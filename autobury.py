import urllib
import urllib.request
import json
from py_ankiconnect import PyAnkiconnect

ankiconnect = PyAnkiconnect()

not_buried = ankiconnect(action="findCards", query="added:1 is:new -is:buried")
if not_buried:
    #print(f"Burying {len(not_buried)} cards.")
    ankiconnect(action="bury", cards=not_buried)
else:
    # no cards to bury, exiting without printing anything
    raise SystemExit()
