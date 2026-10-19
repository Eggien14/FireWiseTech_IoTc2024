#!/bin/bash
sleep 60
# Firebase settings (not in git), see .env.example
set -a; [ -f /home/pi/documents/Python/Fw_prj/.env ] && . /home/pi/documents/Python/Fw_prj/.env; set +a
/home/pi/documents/Python/myenv/bin/python /home/pi/documents/Python/Fw_prj/main.py
#crontab -e