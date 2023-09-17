import json
import urllib.request
from datetime import datetime

from src.company_item import CompanyItem
from src.company_logo import get_logo
from src.job_filter import is_test_job, is_dev_job, is_dev_ops_job, is_data_job, is_finance_job, is_web3_job, \
    is_security_job, is_compliance_job

companies_url = "https://raw.githubusercontent.com/crypto-jobs-fyi/crawler/main/companies.json"
jobs_url = "https://raw.githubusercontent.com/crypto-jobs-fyi/crawler/main/jobs.json"
jobs_age_url = "https://raw.githubusercontent.com/crypto-jobs-fyi/crawler/main/jobs_age.json"
with urllib.request.urlopen(companies_url) as url:
    company_list_json = json.load(url)
company_list = []
for it in company_list_json:
    company_list.append(CompanyItem(it['company_name'], it['company_url'], it['jobs_url']))

just_date = datetime.date(datetime.now())
with urllib.request.urlopen(jobs_url) as url:
    current_jobs = json.load(url)['data']
with urllib.request.urlopen(jobs_age_url) as url:
    jobs_age = json.load(url)

total_jobs = len(current_jobs)
total_companies = len(company_list)
number_of_companies = f'Number of companies: {total_companies}'
number_of_companies_link = f'<a href="companies.html" target="_blank">{number_of_companies}</a>'
first_line = f'{number_of_companies_link} -> Number of jobs: {total_jobs} Last Updated at: {just_date}'
print(first_line)
num_test = 0
num_dev = 0
num_web3 = 0
num_fin = 0
num_ops = 0
num_data = 0
num_sec = 0
num_comp = 0
for j in current_jobs:
    j_title = j['title']
    if is_dev_job(j_title):
        num_dev = num_dev + 1
    if is_data_job(j_title):
        num_data = num_data + 1
    if is_test_job(j_title):
        num_test = num_test + 1
    if is_web3_job(j_title):
        num_web3 = num_web3 + 1
    if is_finance_job(j_title):
        num_fin = num_fin + 1
    if is_dev_ops_job(j_title):
        num_ops = num_ops + 1
    if is_security_job(j_title):
        num_sec = num_sec + 1
    if is_compliance_job(j_title):
        num_comp = num_comp + 1

print(f'>>> Numer of Dev jobs: {num_dev}')
print(f'>>> Numer of Data jobs: {num_data}')
print(f'>>> Numer of Test jobs: {num_test}')
print(f'>>> Numer of Finance jobs: {num_fin}')
print(f'>>> Numer of Compliance jobs: {num_comp}')


def center_td(text):
    return f"<td align='center'>{text}</td>"


with open('index.html', 'w') as f:
    f.write(
        f'<p align="center"> {first_line} </p>')
    eth_wallet_link = '<a href="https://etherscan.io/address/0x589a0d87d600a6c6faa34c491c9e779f434bc51d" ' \
                      'target="_blank">0x589a0D87d600a6C6fAa34c491C9e779f434bC51d</a>'
    f.write(f'<p align="center"> If you find this page useful please donate ETH/ERC-20* to {eth_wallet_link} </p>')
    f.write(f'<p align="center"> *On Etherium, Arbitrum, Optimism or Polygon </p>')
    table_link = '<a href="table.html"> View as Table </a>'
    daily_link = '<a href="daily.html"> Daily as Table </a>'
    f.write(f'<p align="center"> || {table_link} || {daily_link} ||</p>')
    test_link = '<th width=11% bgcolor="lightgreen"><a href="test.html" target="_blank">Test jobs</a></th>'
    dev_link = '<th width=11% bgcolor="lightblue"><a href="dev.html" target="_blank">Dev jobs</a></th>'
    web3_link = '<th width=11% bgcolor="DeepSkyBlue"><a href="web3.html" target="_blank">Web3 jobs</a></th>'
    finance_link = '<th width=11% bgcolor="MediumOrchid"><a href="finance.html" target="_blank">Finance jobs</a></th>'
    devops_link = '<th width=11% bgcolor="lightyellow"><a href="devops.html" target="_blank">DevOps/SRE jobs</a></th>'
    data_link = '<th width=11% bgcolor="cyan"><a href="data.html" target="_blank">Data jobs</a></th>'
    security_link = '<th width=11% bgcolor="Khaki"><a href="security.html" target="_blank">Security jobs</a></th>'
    compliance_link = '<th width=11% bgcolor="MediumPurple"><a href="compliance.html" target="_blank">Compliance jobs</a></th>'
    links = [test_link, dev_link, web3_link, finance_link, devops_link, data_link, security_link, compliance_link]
    joined_links = f"<tr>{''.join(links)}</tr>"
    joined_nums = f"<tr>{center_td(num_test)}{center_td(num_dev)}{center_td(num_web3)}{center_td(num_fin)}{center_td(num_ops)}{center_td(num_data)}{center_td(num_sec)}{center_td(num_comp)}</tr>"
    f.write(f"<table width='78%' align='center' border=1>{joined_links}{joined_nums}</table>")
    f.write(f'<p align="center"> </p>')
with open('test.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('dev.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('devops.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('finance.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('web3.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('data.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('security.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('compliance.html', 'w') as f:
    f.write('<!DOCTYPE html>')


def set_color(title):
    if is_test_job(title):
        return ' bgcolor="lightgreen" '
    elif is_dev_job(title):
        return ' bgcolor="lightblue" '
    elif is_dev_ops_job(title):
        return ' bgcolor="lightyellow" '
    elif is_data_job(title):
        return ' bgcolor="cyan" '
    elif is_finance_job(title):
        return ' bgcolor="MediumOrchid" '
    elif is_web3_job(title):
        return ' bgcolor="DeepSkyBlue" '
    elif is_security_job(title):
        return ' bgcolor="Khaki" '
    elif is_compliance_job(title):
        return ' bgcolor="MediumPurple" '
    else:
        return ""


def dict_to_html_table_with_header(company_item: CompanyItem, job_list, logo=''):
    html_table = '<table width="78%" align="center" border="1">'
    jobs_total = f"Total Jobs: {len(job_list)}"
    header_link = f"<a href='{company_item.company_url}' target='_blank'>{company_item.company_name.upper()}</a>"
    jobs_total_link = f"<a href='{company_item.jobs_url}' target='_blank'> {jobs_total} </a>"
    html_table += f"<tr><th width='20%'> {logo} </th><th> {header_link} </th><th width='4%' align='center'> Age </th><th width='12%'> {jobs_total_link} </th></tr>"
    for elem in job_list:
        color_code = set_color(elem['title'])
        wrapped_link = elem['link']
        location = elem['location']
        job_title = elem['title']
        job_age = jobs_age[elem['link']]
        job_age_title = f"title='{job_age} day(s)'"
        job_link_td = f"<td width='12%' align='center' {job_age_title}>{wrapped_link}</td>"
        html_table += f"<tr {color_code}><td width='22%'>{location}</td><td>{job_title}</td><td align='center'>{job_age}</td>{job_link_td}</tr>"
    html_table += "</table>"
    return html_table


def dict_to_html_table_with_header_and_filter(company_name, job_list, filter):
    filtered = []
    for elem in job_list:
        if filter(elem['title']):
            filtered.append(elem)

    if len(filtered) > 0:
        jobs_total = f"Total {filter.__name__}(s): {len(filtered)}"
        print(f'[BUILDER] {jobs_total} at {company_name}')
    else:
        print(f'[BUILDER] no jobs filtered by {filter.__name__} at {company_name}')
        return ''

    html_table = '<table width="78%" align="center" border="1">'
    html_table += f"<tr><th width='22%'> Location </th><th>" + company_name.upper() + "</th><th width='12%' >" + jobs_total + "</th></tr>"

    for elem in filtered:
        wrapped_link = elem['link']
        location = elem['location']
        job_title = elem['title']
        html_table += f"<tr><td width='22%'>{location}</td><td>{job_title}</td><td width='12%' align='center'>{wrapped_link}</td></tr>"

    html_table += "</table>"
    return html_table


def add_jobs_to_index(company_item: CompanyItem, jobs_data, logo):
    html = dict_to_html_table_with_header(company_item, jobs_data, logo)
    with open('index.html', 'a') as index_file:
        index_file.write(html)


def add_jobs_to_test(company_item: CompanyItem, jobs_data):
    html = dict_to_html_table_with_header_and_filter(company_item.company_name, jobs_data, filter=is_test_job)
    with open('test.html', 'a') as test_file:
        test_file.write(html)


def add_jobs_to_dev(company_item: CompanyItem, jobs_data):
    html = dict_to_html_table_with_header_and_filter(company_item.company_name, jobs_data, filter=is_dev_job)
    with open('dev.html', 'a') as dev_file:
        dev_file.write(html)


def add_jobs_to_dev_ops(company_item: CompanyItem, jobs_data):
    html = dict_to_html_table_with_header_and_filter(company_item.company_name, jobs_data, filter=is_dev_ops_job)
    with open('devops.html', 'a') as devops_file:
        devops_file.write(html)


def add_jobs_to_data(company_item: CompanyItem, jobs_data):
    html = dict_to_html_table_with_header_and_filter(company_item.company_name, jobs_data, filter=is_data_job)
    with open('data.html', 'a') as data_file:
        data_file.write(html)


def add_jobs_to_finance(company_item: CompanyItem, jobs_data):
    html = dict_to_html_table_with_header_and_filter(company_item.company_name, jobs_data, filter=is_finance_job)
    with open('finance.html', 'a') as finance_file:
        finance_file.write(html)


def add_jobs_to_web3(company_item: CompanyItem, jobs_data):
    html = dict_to_html_table_with_header_and_filter(company_item.company_name, jobs_data, filter=is_web3_job)
    with open('web3.html', 'a') as web3_file:
        web3_file.write(html)


def add_jobs_to_security(company_item: CompanyItem, jobs_data):
    html = dict_to_html_table_with_header_and_filter(company_item.company_name, jobs_data, filter=is_security_job)
    with open('security.html', 'a') as security_file:
        security_file.write(html)


def add_jobs_to_compliance(company_item: CompanyItem, jobs_data):
    html = dict_to_html_table_with_header_and_filter(company_item.company_name, jobs_data, filter=is_security_job)
    with open('compliance.html', 'a') as compliance_file:
        compliance_file.write(html)


for company in company_list:
    company_logo = get_logo(company.company_name)
    company_data = list(filter(lambda jd: jd.get('company') == company.company_name, current_jobs))
    add_jobs_to_index(company, company_data, company_logo)
    add_jobs_to_test(company, company_data)
    add_jobs_to_dev(company, company_data)
    add_jobs_to_dev_ops(company, company_data)
    add_jobs_to_data(company, company_data)
    add_jobs_to_finance(company, company_data)
    add_jobs_to_web3(company, company_data)
    add_jobs_to_security(company, company_data)
    add_jobs_to_compliance(company, company_data)
