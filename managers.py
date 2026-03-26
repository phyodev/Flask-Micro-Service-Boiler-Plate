from db import SessionLocal
from models import User
from schemas import UserCreateSchema
from typing import List

class ManagerBase:
    model = None

    def __init__(self):
        self.session = SessionLocal()

    def create(self, data: dict):
        obj = self.model(**data)
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def get_by_id(self, id: int):
        return self.session.query(self.model).get(id)

    def bulk_create(self, data_list: List[dict]):
        self.session.bulk_insert_mappings(self.model, data_list)
        self.session.commit()


class UserManager(ManagerBase):
    model = User
