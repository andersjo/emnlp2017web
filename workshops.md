---
layout: default
---


<div class="section">
  <h2>Workshops</h2>
  <p>
  The workshops take place on September 7 and 8, just before the main conference.
  </p>

  {% for workshop in site.data.workshops %}
    <div class="row">
      <div class="card-panel">
        <div class="col s12 l3">
          <h5>{{ workshop.nickname }}</h5>
          <div>
            {{ workshop.schedule }}
          </div>
        </div>
        <div class="col s12 l9">
            <h5 style="color: black">{{ workshop.title }}</h5>
            <p><i>{{ workshop.description }}</i></p>

            <p>Organised by: {{ workshop.organizers }}</p>

            <p>
              Contact person: <a href="mailto:{{ workshop.email }}">
              {{ workshop.contact_person }}</a>
            </p>

            <p>Workshop <a href="{{ workshop.website }}">website</a></p>
        </div>
        <div class="clear:both">&nbsp;</div>
      </div>
    </div>

  {% endfor %}

</div>
