#!/bin/bash
# source scripts/configs/quantengine.sh
source venv/bin/activate
# pip install -r requirements.txt
cd restserver
python manage.py migrate
python manage.py runserver 0.0.0.0:8888

