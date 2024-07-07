from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from core.dataclasses.auto_park_dataclass import AutoParkDataClass
from core.dataclasses.user_dataclass import UserDataClass

from apps.auto_parks.models import AutoParkModel


class IsAdminPark(BasePermission):
    def has_permission(self, request: Request, view):
        user: UserDataClass = request.user
        auto_park_id = view.kwargs.get('pk')

        try:
            auto_park: AutoParkDataClass = AutoParkModel.objects.get(pk=auto_park_id)
            if user.id == auto_park.admin_id and user.id != auto_park.manager_id:
                return True
        except AutoParkModel.DoesNotExist:
            pass

        return False
