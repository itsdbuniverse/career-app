import requests
import json

def api_fetch():
  data = requests.get("https://3dce0f53-d44b-4a00-9e9f-1bf445d50f11-00-qs9f2kiivs06.sisko.replit.dev/api/jobs")
  data = data.json()
  return data