from urllib.request import urlopen
import time
import sys
import os

time.sleep(10)

url = os.environ['SERVICE_INTERNAL_URL']
for i in range(5):
    print(url)
    with urlopen("http://" + url + ":5000/") as response:
        if response.read().decode("utf-8") != "Hello, World!":
            print("Did not return correctly.")
            os.exit(1)
    time.sleep(1)
print("Test completed correctly.")
