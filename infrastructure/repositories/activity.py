from typing import Optional, List, Protocol
from ..models.activity import Activity
from core.models.activity import Activity as ActivityEntity


class IActivityRepository(Protocol):
    def all(self) -> List[ActivityEntity]:
        pass

    def get(self, id: int) -> Optional[ActivityEntity]:
        pass

    def create(self, activity: ActivityEntity) -> ActivityEntity:
        pass

    def update(self, activity: ActivityEntity) -> ActivityEntity:
        pass

    def delete(self, id) -> None:
        pass


class ActivityRepository:
    def all(self) -> List[ActivityEntity]:
        return [self._convert_instance(activity) for activity in Activity.objects.all()]

    def get(self, id: int) -> Optional[ActivityEntity]:
        if id is None:
            return None

        return self._convert_instance(Activity.objects.filter(id=id).first())

    def create(self, activity: ActivityEntity) -> ActivityEntity:
        new_activity = Activity.objects.create(**activity.__dict__)
        new_activity.save()

        return self._convert_instance(new_activity)

    def update(self, activity: ActivityEntity) -> ActivityEntity:

        Activity.objects.filter(id=activity.id).update(**activity.__dict__)
        activity_updated = Activity.objects.filter(id=activity.id).first()

        return self._convert_instance(activity_updated)

    def delete(self, id) -> None:
        Activity.objects.filter(id=id).delete()

    @staticmethod
    def _convert_instance(instance: Activity) -> ActivityEntity:
        return ActivityEntity(
            id=instance.id,
            due_date=instance.due_date,
            description=instance.description,
            customer_id=instance.customer_id,
        )
