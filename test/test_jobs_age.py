import json
import urllib.request

jobs_age_url = "https://raw.githubusercontent.com/crypto-jobs-fyi/crawler/main/jobs_age.json"
with urllib.request.urlopen(jobs_age_url) as url:
    data = json.load(url)

test = "<a href='https://boards.greenhouse.io/grayscaleinvestments/jobs/5659998003' target='_blank' >Apply</a>"
print(f'Number of records: {len(data)}')
print(f'Test record: {data[test]}')
