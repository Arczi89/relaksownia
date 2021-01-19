#!/bin/bash

cd ~; 
source DemositeEnv/bin/activate; 
cd ~/websites/demosite;
python manage.py retrieve_reviews 2> /home/arturszwagrzak/websites/demosite/cron.log
