import pandas as pd
import re

def rename_column(old_name):
    return str(old_name).lower().replace(" ", "_")

def first_author_last_name(author_names):
    first_author = re.split(r"(,|\band\b)", author_names)[0]
    last_name = first_author.strip().split(" ")[-1].lower()
    return last_name


D = pd.read_excel("accepted_papers.xls")
D = D.rename_axis(rename_column, axis='columns')
D['first_author_last_name'] = D.authors.map(first_author_last_name)
D['submission_type'] = D.submission_type.str.split().str[0]
D = D.sort_values(by="first_author_last_name")

print(D.to_csv('_data/accepted_papers.csv'))
