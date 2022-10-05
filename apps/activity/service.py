import re
from typing import Protocol, List, Optional
from core.models.activity import Activity
from infrastructure.repositories.activity import IActivityRepository


class IActivityService(Protocol):
    def all(self) -> List[Activity]:
        pass

    def get(self, id: int) -> Optional[Activity]:
        pass

    def create(self, activity: Activity) -> Activity:
        pass

    def update(self, activity: Activity) -> Activity:
        pass

    def delete(self, id: int) -> None:
        pass


class ActivityService:
    def __init__(self, repo: IActivityRepository) -> None:
        self.repo = repo

    def all(self) -> List[Activity]:
        return self.repo.all()

    def get(self, id: int) -> Optional[Activity]:
        return self.repo.get(id)

    def create(self, activity: Activity) -> Activity:
        return self.repo.create(activity)

    def update(self, activity: Activity) -> Activity:
        return self.repo.update(activity)

    def delete(self, id: int) -> None:
        self.repo.delete(id)
