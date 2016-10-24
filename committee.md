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
                <b>{{ member.name }}</b> <br/>
                <i>{{ member.affilition }}</i>
              </div>
            {% endfor %}
        </div>
    </div>

  {% endfor %}

</div>
