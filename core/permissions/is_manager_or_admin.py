from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from apps.auto_parks.models import AutoParkModel


class IsManagerOrAdminPark(BasePermission):
    def has_permission(self, request: Request, view):
        user = request.user
        auto_park_id = view.kwargs.get('pk')

        try:
            auto_park = AutoParkModel.objects.get(pk=auto_park_id)

            if user.id == auto_park.manager_id or user.id == auto_park.admin_id:
                return True
        except AutoParkModel.DoesNotExist:
            pass

        return False
