from dataclasses import dataclass


@dataclass(init=True)
class CompanyItem:
    company_name: str
    company_url: str
    jobs_url: str
