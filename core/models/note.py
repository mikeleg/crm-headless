from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Note:
    id: Optional[int]
    description: str
    customer_id: Optional[int]
