#!/bin/bash

# Replace "/path/to/venv" with the actual path to your virtual environment
source ~/dev/crontab/script/punch/bin/activate

# Replace "your_python_app.py" with the actual name of your Python application script
python3 ~/dev/crontab/script/punch/main.py

# Deactivate the virtual environment
deactivate
