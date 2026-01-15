from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ChecklistItem(BaseModel):
    id: str
    text: str
    is_completed: bool = False
    created_at: datetime = datetime.now()

class Checklist(BaseModel):
    id: str
    title: str
    owner_id: str
    items: List[ChecklistItem] = []
    created_at: datetime = datetime.now()
