import requests
from time import sleep
import subprocess

url = "https://www.google.com"
timeout = 10


def connect_to_network():
    process = subprocess.Popen(
        'netsh wlan connect name=FTTH_LI6670_5GHz',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()


while 1:
    try:
        request = requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
        connect_to_network()
        sleep(3)
    sleep(0.5)
