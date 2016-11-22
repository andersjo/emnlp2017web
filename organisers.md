---
layout: default
---


<div class="section">
  <h2>Organizing committee</h2>
  {% for group in site.data.organizing_committee %}

    <div class="row">
        <div class="col s4">
          <h5>{{ group.title }}</h5>
        </div>
        <div class="col s8">
            {% for member in group.members %}
              <div class="card-panel">
              <div class="right">
                <a href="{{ member.site }}"><i class="material-icons">person_pin</i></a>
                <a href="mailto:{{ member.email }}"><i class="material-icons">email</i></a>
              </div>
              <b>{{ member.name }}</b> <br/>
              <i>{{ member.affiliation }}</i>
              </div>
            {% endfor %}
        </div>
    </div>

  {% endfor %}

</div>
