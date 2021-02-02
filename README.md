# intercom


[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badge/)



## Problem definition
Given a list of customers find customers within 100km of Intercom Dublin office.

## How to CI
![Pytest Intercom app](https://github.com/brufen/intercom/workflows/Pytest%20Intercom%20app/badge.svg)

Continuous integration is implemented via github [actions](https://github.com/brufen/intercom/actions) on every code push. 

## How to run

cd to project root
```
pip install -r requirements.txt
python app.py
```
## How to test

cd to project root
```
pip install pytest
pip install pytest-cov
pytest
```
[Check out test coverage](https://github.com/brufen/intercom/runs/1816057811?check_suite_focus=true)

## Build script

cd to project root
```
./build_scripts/build_service.sh
```

## Output file with results
[Ouput json](https://github.com/brufen/intercom/blob/master/src/output/output.json)


## Author
Marija
