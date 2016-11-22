---
layout: default
---


<div class="section">
  <h2>Area chairs</h2>
  {% for group in site.data.area_chairs %}

    <div class="row">
        <div class="col s12 l4">
          <h5>{{ group.title }}</h5>
        </div>
        <div class="col l8 s12">
            {% for member in group.members %}
              <div class="card-panel">
              <div class="right">
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
