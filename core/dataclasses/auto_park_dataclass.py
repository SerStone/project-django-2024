from dataclasses import dataclass
from datetime import datetime


@dataclass
class AutoParkDataClass:
    id: int
    name: str
    manager_id: int
    admin_id: int
    salesperson_id: int
    mechanic_id: int
    created_at: datetime
    updated_at: datetime
