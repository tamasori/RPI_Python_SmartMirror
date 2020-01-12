import subprocess
import pymongo

from datetime import datetime

val = subprocess.check_output("python3 /home/pi/Okostukor/homeres.py", shell=True)

val = val.decode("ascii").strip()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["tukor"]

now = datetime.now()

record = {"date": now.strftime("%Y.%m.%-d. %H:%M"), "temperature": val}

db["homeres"].insert_one(record)

if float(val) < 18.0:
	subprocess.call('python3 /home/pi/Okostukor/tweet.py "@tams_ri Leesett a hőmérséklet a szobádban {0}°C fokra. Talán nyitvahagytad az ablakot?"'.format(val), shell=True)
	
if float(val) > 26.0:
	subprocess.call('python3 /home/pi/Okostukor/tweet.py "@tams_ri Felszökött a hőmérséklet a szobádban {0}°C fokra. Talán elfelejtetted lekapcsolni a fűtést?"'.format(val), shell=True)
