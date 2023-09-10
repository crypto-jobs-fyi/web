def filter_jobs(job_title: str, filters):
    if any(ext.lower() in job_title.lower() for ext in filters):
        return True
    return False


def is_dev_job(title):
    tags = [
        'Node.js Engineer',
        'software engineer',
        'stack engineer',
        'systems engineer',
        'System Engineer',
        'java engineer',
        'backend engineer',
        'backend developer',
        'java developer',
        'rust engineer',
        'golang engineer',
        'principal engineer',
        'back-end engineer',
        'senior java',
        'staff engineer',
        'api engineer',
        'rust developer',
        'full stack developer',
        'c++ developer',
        'full-stack dev',
        'python developer',
        'java development lead',
        'python dev', 'Go Engineer',
        'Golang Developer',
        'Engineer - Java',
        'Java Development Engineer',
        'Frontend Developer',
        'Software Development Engineer',
        'Software Architect',
        'Frontend Engineer',
        'Front End Developer',
        'Frontend Architect ',
        'Front-end Developer',
        'Web Developer',
        'Front-End Engineer',
        'Lead Engineer',
        'Fullstack Developer',
        'Solutions Engineer',
        'Compiler Engineer',
        '(Front-End) Engineer',
        'Solutions Engineer',
        'TypeScript Toolkit Engineer',
        'Technical Lead',
        'Backend / Fullstack',
        'Front End Architect',
        'Solution Architect ',
        'Golang Team Lead',
        'Senior Engineer, Frontend',
        'C++ Engineer', 'UI/UX Developer',
        'Indexer Engineer', 'Python/C++',
        'Mobile Engineer',
        'Senior Engineer – Java',
        'React Native Engineer',
        'iOS Developer', 'Android Developer',
        'iOS Engineer', 'Android Engineer',
        'Scala Engineer',
        'Wordpress Developer',
        'Application Engineer',
        'Compiler/Language Engineer',
        'Front End Engineer',
        'Front-End'
    ]
    result = filter_jobs(title, tags)
    anti_filters = ['test', 'qa', 'manager', 'sdet', 'director']
    if any(ext.lower() in title.lower() for ext in anti_filters):
        return False
    return result


def is_test_job(title):
    tags = ['qa', 'test', 'sdet', 'quality assurance']
    result = filter_jobs(title, tags)
    anti_filters = ['manager', 'director', 'head']
    if any(ext.lower() in title.lower() for ext in anti_filters):
        return False
    return result


def is_web3_job(title):
    tags = ['Blockchain Developer', 'Cryptography Engineer', 'Protocol Engineer', 'Protocol Research',
            'Zero Knowledge Research Engineer', 'Smart Contract Engineer', 'Blockchain Engineer',
            'Blockchain Client Engineer', 'Cryptographer', 'Blockchain Integration Specialist',
            'Solidity Developer', 'Web3 developer', 'Smart Contract Developer', 'Engineer - Smart Contract',
            'Cryptography Researcher', 'Backend/Solidity', 'Solana/Rust', 'ZK Circuits', 'Solidity Engineer',
            'Research Engineer', 'Zero-Knowledge Proof', 'DeFi Lead', 'Cryptographic Engineer', 'Consensus Engineer']
    result = filter_jobs(title, tags)
    anti_filters = ['director', 'head']
    if any(ext.lower() in title.lower() for ext in anti_filters):
        return False
    return result


def is_finance_job(title):
    tags = ['Accountant', 'Treasury', 'Finance', 'Accounting', 'Tax Specialist', 'Financial', 'FinCrime',
            'Accounts Payable', 'Treasurer', 'Payroll Specialist', 'Corporate Controller', 'Tax Analyst',
            'Accounts Receivable', 'Payroll Coordinator', 'Revenue Analyst', 'Deputy Controller']
    result = filter_jobs(title, tags)
    anti_filters = ['manager', 'director', 'head of', 'Scientist', 'Engineer']
    if any(ext.lower() in title.lower() for ext in anti_filters):
        return False
    return result


def is_dev_ops_job(title):
    tags = [
        'devops', 'sre',
        'Dev Ops Engineer',
        'site reliability',
        'platforms engineer',
        'infrastructure engineer',
        'network engineer',
        'Platform Engineer',
        'Tooling Engineer',
        'Infrastructure Development Engineer',
        'Infrastructure & Tooling',
        'Release Automation Engineer',
        'Kubernetes Engineer'
    ]
    result = filter_jobs(title, tags)
    anti_filters = ['test', 'qa', 'manager', 'sdet', 'director']
    if any(ext.lower() in title.lower() for ext in anti_filters):
        return False
    return result


def is_security_job(title):
    tags = [
        'Cloud Security Engineer',
        'Security Engineer',
        'Security Response Engineer',
        'Security Lead',
        'Cyber Threat', 'SecOps Engineer'
    ]
    result = filter_jobs(title, tags)
    anti_filters = ['test', 'qa', 'manager', 'sdet', 'director', 'counsel']
    if any(ext.lower() in title.lower() for ext in anti_filters):
        return False
    return result


def is_data_job(title):
    tags = ['Data Engineer', 'Data Analyst', 'Data Scientist', 'Data Engineer', 'Data Analytics Engineer',
            'Data Science', 'DataOps Engineer']
    return filter_jobs(title, tags)


def is_compliance_job(title):
    tags = ['Compliance Analyst', 'Compliance Manager', 'Compliance Associate', 'Compliance Officer',
            'Compliance and Risk Officer', 'Compliance Specialist', 'Compliance Assistant', 'Compliance Lead']
    return filter_jobs(title, tags)
