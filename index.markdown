---
layout: article
title: Rocket Clubs
---

# Rocket Clubs Around The World

This is not yet an exhaustive list. This is a list of small time projects that
I find particularly exiting or advanced. It's mostly student groups at
Universities. That said, if you see something you think is missing,
[send a pull request](https://github.com/natronics/Rocket-Clubs)!

Download a yaml file of this data: [groups.yml](https://github.com/natronics/Rocket-Clubs/raw/gh-pages/_data/groups.yml)


--------------------------------------------------------------------------------

<div class="columns">
 <div class="column">
  <h2>University Clubs</h2>
   <ul>
    {% for club in site.data.groups['clubs'] %}
      <li><a href="#{{ club.shortname | downcase | replace:' ', '-' | replace:'@', '' }}">{{ club.shortname }}</a></li>
    {% endfor %}
   </ul>
  </div>
  <div class="column">
   <h2>Independent</h2>
    {% for club in site.data.groups['groups'] %}
      <li><a href="">{{ club.shortname }}</a></li>
    {% endfor %}
 </div>
</div>

---------------


# University Clubs

<div class="columns is-multiline" markdown="1">

{% for club in site.data.groups['clubs'] %}

<div class="column is-third" markdown="1">

### {{ club.shortname }}

_{{ club.name }}_, {{ club.location.name }}

<ul>
 <li><a href="{{ club.homepage }}">{{ club.homepage }}</a></li>
 {% for link in club.links %}
 <li><a href="{{ link.url }}">{{ link.title }}</a></li>
 {% endfor %}
</ul>

**Major Project**: {{ club.project }}

</div>

{% endfor %}
</div>

# Independent Clubs


{% for club in site.data.groups['groups'] %}
### {{ club.shortname }}

_{{ club.name }}_, {{ club.location.name }}

<ul>
 <li><a href="{{ club.homepage }}">{{ club.homepage }}</a></li>
 {% for link in club.links %}
 <li><a href="{{ link.url }}">{{ link.title }}</a></li>
 {% endfor %}
</ul>

**Major Project**: {{ club.project }}

{% endfor %}
