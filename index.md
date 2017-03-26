---
layout: default
---

<div class="section">
  <h3>Announcements</h3>
</div>

  <ul class="collection">
    <li class="collection-item avatar">
      <i class="material-icons circle">info_outline</i>
      <span class="title"><big>EMNLP 2017 announced</big></span>
      <p>Next year's EMNLP will take place in Copenhagen.
      The main conference is September 9 - 11, preceded by two days of workshops and tutorials,
      September 7 - 8. See <a href="call-for-papers.html">call for papers</a>.
      <br>
      <span class="right-align">
         <i>Posted on November 22, 2016</i>
      </span>
      </p>
    </li>

  </ul>

<div id="calendar" class="section">
  <h3>Important dates</h3>

  <table class="striped deadline">
    <thead>
      <tr>
          <th data-field="event">Deadline</th>
          <th data-field="date">Date</th>
      </tr>
    </thead>
    <tbody>

      {% for deadline in site.data.deadlines %}
        <tr>
            <td>{{ deadline.title }}</td>
            <td><time>{{ deadline.datetime | date: '%B %d, %Y' }}</time></td>
        </tr>
      {% endfor %}
    </tbody>
  </table>


  <div class="center-align" style="margin-top: 1em;">
    All the above deadlines are 11:59pm Pacific Daylight Savings Time (UTC -7h).
  </div>

  <br/>

  <table class="striped event">
    <thead>
      <tr>
          <th style="width: 50%" data-field="event">Event</th>
          <th data-field="date">Date</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Workshops and tutorials</td>
        <td><time>September 7 and 8, 2017</time></td>
      </tr>
      <tr>
        <td>Main conference</td>
        <td><time>September 9 - 11, 2017 </time></td>
      </tr>
    </tbody>
    </table>

</div>

<div id="sponsors" class="section">


{% for sponsor_group in site.data.sponsors %}
  <div class="sponsor-group center-align">
  <h4 style="clear: both;">{{ sponsor_group.category }}</h4>



  <ul>
  {% for sponsor in sponsor_group.members %}
    <li>
       <a href="#{{ sponsor.name }}"><img alt="{{ sponsor.name }}" src="logos/{{ sponsor.shortname }}.png" style="width:200px !important"/></a>
    </li>

  {% endfor %}
  </ul>
  </div>


{% endfor %}




<div style="clear: both"></div>
</div>


<!--
<div id="contacts" class="section">
  <h2>Collocated Events</h2>
  <p>
  EMNLP 2016 is collocated with <a href="	http://amtaweb.org/amta-2016-in-austin-tx">AMTA 2016</a>, hosted by the Association for Machine Translation in the Americas from October 28 to November 1, 2016.
  </p>
  <p>
  <a href="http://www.humancomputation.com/2016/">HCOMP 2016</a>, the 4th AAAI Conference on Human Computation and Crowdsourcing  will also be held in Austin, TX with main conference on October 30 to November 3.
  </p>
</div>
!-->
