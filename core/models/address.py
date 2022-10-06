from dataclasses import dataclass
from typing import Optional


@dataclass
class Address:
    id: Optional[int]
    nickname: Optional[str]
    street: str
    number: int
    city: str
    zip_code: str
    country: str
    customer_id: Optional[int]
    contact_id: Optional[int]
