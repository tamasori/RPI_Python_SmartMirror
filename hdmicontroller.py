import subprocess
import time
import os

time.sleep(60)

while True:
    val = subprocess.check_output("python3 /home/pi/Okostukor/ultrasonic.py 100", shell=True)
    val= val.decode('ascii')
    if val == 'True\n':
        print('tr')
        subprocess.call('vcgencmd display_power 1', shell=True)
        time.sleep(120)
    else:
        hdmi =subprocess.check_output("vcgencmd display_power", shell=True).decode('ascii')
        if(hdmi == 'display_power=1\n'):
            print("sleeping")
            subprocess.call('vcgencmd display_power 0', shell=True)
    time.sleep(0.5)
