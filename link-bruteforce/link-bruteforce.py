import requests
import string
import re
import time

alphabet = '-_' + string.ascii_letters + string.digits
found_ids = []

for c in alphabet:

    id = f'AAAAAAAAAA{c}'
    r = requests.get('https://youtube.com/watch?v=' + id)
    assert(r.status_code == 200)

    title = re.findall(r'<title>(.*?)</title>', r.text)[0]
    print(id)
    print(title)

    if title != ' - YouTube':
        found_ids.append(id)

    time.sleep(0.3)

print('Found ids: ', found_ids)