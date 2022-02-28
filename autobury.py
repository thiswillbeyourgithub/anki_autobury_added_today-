import urllib
import urllib.request
import json

def ankiconnect(action, **params):
    """
    used to send request to anki using the addon anki-connect
    """
    def request_wrapper(action, **params):
        return {'action': action, 'params': params, 'version': 6}

    requestJson = json.dumps(request_wrapper(action, **params)
                             ).encode('utf-8')
    try:
        response = json.load(urllib.request.urlopen(
            urllib.request.Request(
                'http://localhost:8775',
                requestJson)))
    except (ConnectionRefusedError, urllib.error.URLError) as e:
        # Anki is probably not running, exiting without print
        raise SystemExit()

    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']


not_buried = ankiconnect(action="findCards", query="added:1 is:new -is:buried")
if not_buried:
    #print(f"Burying {len(not_buried)} cards.")
    ankiconnect(action="bury", cards=not_buried)
else:
    # no cards to bury, exiting without printing anything
    raise SystemExit()
