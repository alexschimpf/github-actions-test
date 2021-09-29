import sys
import time
import requests

MAX_TIMEOUT = 60

start_time = time.time()
while time.time() - start_time < MAX_TIMEOUT:
    print('Attempting request...')

    try:
        response = requests.get('http://localhost:1080/mockserver/dashboard')
    except Exception:
        pass
    else:
        if response.status_code == 200:
            print('Success!')
            sys.exit()

    print('Sleeping...')
    time.sleep(5)

print('Failure!!')
sys.exit(1)
