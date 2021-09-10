import sys
import time
import requests

MAX_TIMEOUT = 60

start_time = time.time()
while time.time() - start_time < MAX_TIMEOUT:
    response = requests.get('http://localhost:1080/mockserver/dashboard')
    if response.status_code == 200:
        sys.exit()

sys.exit(1)
