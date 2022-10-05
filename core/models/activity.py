from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Activity:
    id: Optional[int]
    description: str
    due_date: datetime
    customer_id: Optional[int]
