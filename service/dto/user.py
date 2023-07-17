from dataclasses import dataclass
from datetime import date, datetime

@dataclass(slots=True)
class User:
    id:id=0
    username:str=''
    bio:str=''
    created_at:date=datetime.today().date()