import json
import urllib.request
import ssl
from src.company_item import CompanyItem

context = ssl._create_unverified_context()
companies_url = "https://raw.githubusercontent.com/crypto-jobs-fyi/crawler/main/companies.json"
with urllib.request.urlopen(companies_url, context=context) as url:
    data = json.load(url)

print(f'Number of companies: {len(data)}')
print(f'First company: {data[0]}')
print(f'First company name: {data[0]["company_name"]}')
re = []
for it in data:
    re.append(CompanyItem(it['company_name'], it['company_url'], it['jobs_url']))
print(f'Number of companies: {len(re)}')
print(f'First company: {re[0]}')
