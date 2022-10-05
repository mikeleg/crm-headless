from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Contact:
    id: Optional[int]
    name: str
    surname: str
    email: str
    phone: str
    job_title: str
    customer_id: Optional[int]
