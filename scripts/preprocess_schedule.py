import argparse
from pathlib import Path
from datetime import datetime, timedelta, timezone

import pandas as pd
import re
from itertools import groupby
import yaml
import json
# from ruamel import yaml

parser = argparse.ArgumentParser(description="Converts from custom 'order' format to YAML")
parser.add_argument("schedule_file", help="A CSV dump from ScheduleMaker", type=Path)
parser.add_argument("submission_file", help="Submission information file", type=Path)
parser.add_argument("--out", help="The output file", type=Path)
# parser.add_argument("--output-dir",
#                     help="Place output files here (default is tests/integration-tests/generated)",
#                     type=Path,
#                     default=CACHE_DIR)
# parser.add_argument("--input-dir",
#                     help="Read input files here (default is tests/integration_tests/definitions)",
#                     type=Path,
#                     default=DEFINITIONS_DIR)
# parser.add_argument('--wiri-url', help="URL for wiri (default: use deployed orchard version)",
#                     default=WIRI_URL)
# parser.add_argument('--verbose', '-v', help="Turns on more verbose logging", action='store_true')
# parser.add_argument('--no-generate-user-signal', '--no-wiri',
#                     help="When defined don't call to wiri",
#                     dest='generate_user_signal',
#                     action='store_false')
args = parser.parse_args()

def rename_column(old_name):
    return str(old_name).lower().replace(" ", "_").replace('_(ignored)', '')

def date_str_to_datetime(date_str):
    time_without_tz = datetime.strptime(date_str, "%A, %B %d, %Y")
    cph_tz = timezone(timedelta(hours=2))
    return time_without_tz.replace(tzinfo=cph_tz)

def time_str_to_delta(time_str):
    abs_time = datetime.strptime(time_str, "%H:%M")
    return timedelta(hours=abs_time.hour, minutes=abs_time.minute)

# Load schedule
NA_VALUE = '(.)'
D = pd.read_csv(args.schedule_file, dtype=str)
D = D.rename_axis(rename_column, axis='columns')
D = D.where((pd.notnull(D)), None)

# Load submissions
submissions = pd.read_csv(args.submission_file, dtype=str)
submissions = submissions.rename_axis(rename_column, axis='columns')
submissions = submissions.where((pd.notnull(submissions)), None)
submission_by_id = {rec['submission_id']: rec
                    for rec in submissions.to_dict('records')}

days = []
session = []
day_program = []

current_date = None
session_id = 1
for rec in D.to_dict('records'):
    if rec['day_date']:
        current_date = date_str_to_datetime(rec['day_date'])
        day_program = []
        days.append({'day': rec['day_date'],
                     'program': day_program,
                     'weekday': rec['day_date'].split(",")[0]
                     })
    elif rec['ses_title']:
        start_time_delta = time_str_to_delta(rec['ses_time'])
        end_time_delta = time_str_to_delta(rec['ses_end_time'])
        start_time = current_date + start_time_delta
        end_time = current_date + end_time_delta

        session = {
            'title': rec['ses_title'],
            'start_time': rec['ses_time'],
            'end_time': rec['ses_end_time'],
            'start_time_iso': start_time.isoformat(),
            'end_time_iso': end_time.isoformat(),
            'room': rec['ses_room'] if rec['ses_room'] != NA_VALUE else None,
            'code': rec['ses_code'] if rec['ses_code'] != NA_VALUE else None,
            'talks': [],
            'posters': [],
            'id': str(session_id)
        }

        day_program.append(session)
        field_map = {'ses_chair': 'chair', 'ses_chair_aff': 'chair_affiliation'}
        for old_field in field_map.keys():
            if rec[old_field] != '(.)':
                session[field_map[old_field]] = rec[old_field]

        session_id += 1

    elif rec['pap_id']:
        paper = {'id': rec['pap_id']}

        if 'Accept-TACL' in rec['pap_status']:
            paper['venue'] = 'TACL'
        else:
            paper['venue'] = 'ACL'

        if rec['pap_time'] != NA_VALUE:
            paper['start_time'] = str(rec['pap_time'])
            paper['end_time'] = str(rec['pap_end_time'])

        # Submission
        submission = submission_by_id[rec['pap_id']]
        paper['title'] = submission['title']
        paper['authors'] = submission['authors']
        paper['abstract'] = submission['summary']

        if 'start_time' in paper:
            session['talks'].append(paper)
        else:
            session['posters'].append(paper)

    elif rec['gen_title']:
# gen_title': 'Physical simulation, learning and language', 'gen_presenter': 'Nando de Freitas', 'gen_time': '09:00', 'gen_end_time': '10:00'
        allowed_events = ['Coffee', 'Break', 'Lunch']
        if not any(event in rec['gen_title'] for event in allowed_events):
            continue

        if rec['gen_time'] == "(.)" or rec['gen_end_time'] == "(.)":
            print("Failed to export end time", rec)
            continue

        start_time_delta = time_str_to_delta(rec['gen_time'])
        end_time_delta = time_str_to_delta(rec['gen_end_time'])
        start_time = current_date + start_time_delta
        end_time = current_date + end_time_delta

        general = {
            'title': rec['gen_title'],
            'start_time': rec['gen_time'],
            'end_time': rec['gen_end_time'],
            'start_time_iso': start_time.isoformat(),
            'end_time_iso': end_time.isoformat(),
            'id': str(session_id)
        }

        session_id += 1


        # invited_speakers = ['Nando de Freitas', 'Sharon Goldwater', 'Dan Jurafsky']
        #
        # if rec['gen_presenter'] in invited_speakers:
        #     continue


        day_program.append(general)

# Group by start time
def make_tracks(program):
    tracks = []
    for start_time, g in groupby(program, key=lambda s: s['start_time']):
        tracks.append(list(g))
    return tracks

def classify_session(session):
    if 'talks' in session and len(session['talks']):
        return 'paper'
    elif 'posters' in session and len(session['posters']):
        return 'poster'
    elif 'Invited Talk' in session['title']:
        return 'invited_talk'
    elif 'Break' in session['title'] or 'Lunch' in session['title'] or 'Coffee' in session['title']:
        return 'break'
    else:
        return 'other'


for day in days:
    day['program'] = make_tracks(day['program'])

    for track in day['program']:

        for session in track:
            session['type'] = classify_session(session)




if args.out:
    # yaml_doc = yaml.dump(days, default_flow_style=False)
    # args.out.write_text(yaml_doc)
    json_doc = json.dumps(days)
    args.out.write_text(json_doc)
