import json
import urllib.request

with urllib.request.urlopen("https://raw.githubusercontent.com/crypto-jobs-fyi/crawler/main/jobs.json") as url:
    data = json.load(url)['data']

print(f'Number of jobs: {len(data)}')
