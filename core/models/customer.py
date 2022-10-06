from dataclasses import dataclass

from typing import Optional

from core.enums import CUSTOMER_TYPE


@dataclass
class Customer:
    id: Optional[int]
    nickname: str
    legalname: str
    vat: str
    address: str
    city: str
    zipcode: str
    country: str
    province: str
    geo: str
    phone: str
    email: str
    pec: str
    sdi: str
    type: "CUSTOMER_TYPE"
