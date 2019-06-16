# WW2API
## Description
<b>What?</b> <br>
WW2API is an API containing all kinds of data about WW2 (planes, ships, guns etc) in Python. 
This project is open-source and people are encouraged to add more and more information to it!

<b>Why?</b> <br>
Because I want to learn more about API’s, Python and lets face it, WW2 is the single most interesting event of the last century. 
This project is inspired by the SWAPI.

<b>How?</b> <br>
Python 3.7, will be django together with djangorestframework.

## Working conventions
**Coding**
- PEP 8!

**Git**
- exclude venv, IDE files, *.pyc

## API
**List of things**
- countries 
- aircraft
- vehicles
- ships
- engines
- weapons
- armies
- manufacturers
- battles
- operations
- theatres

**Design philosophy**
- JSON only.
- Use plurals (/planes instead of /plane)
- GET/POST/DELETE/PUT /planes/id 

##TODO:
 **layout**
 - Come up with a suitable model for aircraft to serve as an example. 
 
# Endpoints
 - Endpoints are specified as the resource + an ID (/planes/109)
 
## Countries

#### Model
| function | method | endpoint | fields | returns |
| --- | --- | --- | --- | --- | 


