from dataclasses import dataclass
from typing import Optional


@dataclass
class Contact:
    id: Optional[int]
    nickname: Optional[str]
    name: str
    surname: str
    email: str
    phone: str
    job_title: str
    customer_id: Optional[int]
