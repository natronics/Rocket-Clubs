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
   <li class="{% for tag in club.tags %}{{tag}} {% endfor %}"><a href="#{{ club.shortname | downcase | replace:' ', '-' | replace:'@', '' }}">{{ club.shortname }}</a></li>
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

### Tags:

Click a tag to highlight:

<p id="taglist">
</p>

--------------------------------------------------------------------------------


# University Clubs

<div class="columns is-multiline" markdown="1">

{% for club in site.data.groups['clubs'] %}

<div class="column is-half {% for tag in club.tags %}{{tag}} {% endfor %}" style="margin-bottom:40px;padding-left:40px;" markdown="1">

<h3 style="border-bottom:1px solid #ccc;" id="{{ club.shortname | downcase | replace:' ', '-' | replace:'@', '' }}">{{ club.shortname }}</h3>

_{{ club.name }}_, {{ club.location.name }}

<ul>
 <li><a href="{{ club.homepage }}">{{ club.homepage }}</a></li>
 {% for link in club.links %}
 <li><a href="{{ link.url }}">{{ link.title }}</a></li>
 {% endfor %}
</ul>

**Major Project**: {{ club.project }}

Tags: {% for tag in club.tags %}<span class="tag">{{ tag }}</span> {% endfor %}

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

<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
<script>
    $( document ).ready(function() {
        var taglist = new Set();

        {% for club in site.data.groups['clubs'] %}
            {% for tag in club.tags %}
                taglist.add("{{ tag }}");
            {% endfor %}
        {% endfor %}

        for (var tag of taglist) {
            $('<a/>', {
                id: tag,
                text: tag,
                class: "tag"
            }).appendTo('#taglist').click(function () {

                // clear highlights
                $('a.tag').css("background-color", "#f5f7fa");
                for (var tag of taglist) {
                    $('.'+tag).css("background-color", "#fff");
                }

                // highlight
                $("."+this.id).css("background-color", "#fed");
                $(this).css("background-color", "#fed");
            });
            $('#taglist').append(" ");
        }

        $('<a/>', {
                id: 'clear',
                text: "Clear Highlights",
                class: "button is-small"
            }).appendTo('#taglist').click(function () {
                // clear highlights
                $('a.tag').css("background-color", "#f5f7fa");
                for (var tag of taglist) {
                    $('.'+tag).css("background-color", "#fff");
                }
         });
    });
</script>
