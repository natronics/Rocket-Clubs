#!/usr/bin/env python
import yaml
import json
import re

DATABASE = 'database.yml'

def build_site():
    """Loop throught data and creat Jekyll markdown"""

    data = {}
    with open(DATABASE, 'r') as f_in:
        data = yaml.load(f_in.read())

    # create list of rockets and sort them by shortname
    clubs = []
    groups = []
    for club, info in data['clubs'].iteritems():
        clubs.append((club, info['shortname']))
    for group, info in data['groups'].iteritems():
        groups.append((group, info['shortname']))
    clubs.sort(key=lambda tup: tup[1])
    groups.sort(key=lambda tup: tup[1])

    # Build Markdown
    page = """---
layout: article
title: Rocket Clubs
---

# Rocket Clubs Around The World

This is not yet an exhaustive list. This is a list of small time projects that
I find particularly exiting or advanced. It's mostly student groups at
Universities. That said, if you see something you think is missing,
[send a pull request](https://github.com/natronics/Rocket-Clubs)!


--------------------------------------------------------------------------------


"""

    # Unviersity Clubs
    page += '<div class="col-sm-4" markdown="1">\n## University Clubs\n\n'
    for club in clubs:
        club = data['clubs'][club[0]]['shortname']
        slug = club.replace(' ', '_')
        slug = re.sub(r'\W+', '', slug).lower()
        page += " - [{0}](#{1})\n".format(club, slug)
    page += "\n</div>\n\n"

    # Independent groups
    page += '<div class="col-sm-4" markdown="1">\n## Independent\n\n'
    for club in groups:
        club = data['groups'][club[0]]['shortname']
        slug = club.replace(' ', '_')
        slug = re.sub(r'\W+', '', slug).lower()
        page += " - [{0}](#{1})\n".format(club, slug)
    page += "\n</div>\n"

    page += "\n\n{.row}\n------------------\n"

    # Full List:
    page += "\n# University Clubs\n\n"

    for club in clubs:
        club = data['clubs'][club[0]]

        # Precompute steps
        links = ""
        for link in club.get('links', []):
            links +=  " - [{0}]({1})\n".format(link['title'], link['url'])

        page += """### {sn}

_{name}_, {loc}

 - <{home}>
{links}

**Major Project**: {proj}


--------------------------------------------------------------------------------


""".format(sn=club['shortname'],
      name=club['name'],
      loc=club['location']['name'],
      home=club['homepage'],
      links=links,
      proj=club['project']
    )

    page += "\n# Independent Clubs\n\n"


    for club in groups:
        club = data['groups'][club[0]]

        # Precompute steps
        links = ""
        for link in club.get('links', []):
            links +=  " - [{0}]({1})\n".format(link['title'], link['url'])

        page += """### {sn}

_{name}_, {loc}

 - <{home}>
{links}

**Major Project**: {proj}


--------------------------------------------------------------------------------


""".format(sn=club['shortname'],
      name=club['name'],
      loc=club['location']['name'],
      home=club['homepage'],
      links=links,
      proj=club['project']
    )


    with open('index.markdown', 'w') as index:
        index.write(page)

if __name__ == '__main__':
    build_site()
