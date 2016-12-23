import requests

resp = requests.get('http://192.168.0.23/api/relay/state')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

print(resp.json())
for item in resp.json():
    #print('{} {}'.format(item['state'], item['relay']))
    state = item['state']
    print(state)
    if  state == 0:
        requests.get('http://192.168.0.23/s/1')
    else:
        requests.get('http://192.168.0.23/s/0')
