# Rocket-Clubs

An attempt at a list of university and small amateur rocket clubs around the world that are building ambitious rocket projects.

## <https://natronics.github.io/Rocket-Clubs/>


## Edit The List

Pull requests welcome! I'm sure I have missing and incomplete data.


### Guide For Inclusion

Just about every university with an engineering program has a rocket club. I'm looking for unusual and ambitious ones. To be on the list they should be doing something like:

 - Serious attempt to to launch higher than 30 km
 - Designing their own liquid-fuel engines
 - Doing something novel with materials (custom carbon fiber, etc.)
 - Custom electronics and avionics with some novel twist (not just a data logger)
 - Active stabilization/controls
 - Publish source (hardware and/or software) publicly

Or similar. These are suggestions, not a strict requirements list, but I hope you see the pattern.


## YAML Stub

The raw data (the list) is in the file `_data/groups.yml`. Simply edit the file and add or update an entry. It's [YAML][yaml], so it should be easy to edit. Here is blank stub for an entry, copy and paste this into the file to add a new group:

```yaml
- shortname: ABBR or acronym for the group
  name: Full name spelled out
  institution: "Private Club" for non-university groups, or the name of the university
  location:
    name: City/state or country
    lat: latitude
    lon: longitude
  homepage: main website for the group
  links:
    - title: "@twitter handle"
      url: https://twitter.com/handle/
    - title: github.com/gihubname
      url: https://github.com/github name
    ... etc. as many as you like (facebook, youtube, blog...)
  project: "Short description of the main projects the club works on, this should highlight the exciting part"
  tags: [avionics, open-source, liquid-engine, high-altitude, etc....]
```

All you need to edit is the data file, then send a Pull Request! The web page will automatically update when it's merged.

[yaml]: http://www.yaml.org/start.html
