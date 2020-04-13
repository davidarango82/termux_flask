from flask import Flask

import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output

app = Flask(__name__)

@app.route('/check')
def check_fetch_sensor_data():
    print('\nchecking sensor data!\n')
    stdout = check_output(['./read_sensor_data_db.sh']).decode('utf-8')
    return stdout

@app.route('/')
def fetch_sensor_data():
    print('\nfetching sensor data!\n')
    session = subprocess.Popen(['./read_sensor_data_db.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')

@app.route('/termux-battery-status')
def check_termux_battery_status():
    print('\nrunning termux-battery-status bash script!\n')
    stdout = check_output(['./termux-battery-status.sh']).decode('utf-8')
    return stdout


