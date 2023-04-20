from dataclasses import dataclass


@dataclass(init=True)
class CompanyItem:
    company_name: str
    jobs_url: str
    company_url: str
    company_type: str
