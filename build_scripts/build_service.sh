#!/bin/bash

cd ..

appname="Intercome app"

echo "pulling changes"
git pull https://brufen:password@git_hostname.com/my/repository


echo "checking for new pip deps"
pip install -r requirements.txt

python app.py
echo "build success"

echo "start $appname success"
