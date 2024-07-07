from django.urls import path

from apps.auto_parks.views import (
    AutoParkAddAdvertisementView,
    AutoParkListCreateView,
    PromoteToAdminPark,
    PromoteToMechanicPark,
    PromoteToSalesmanPark,
    RemoveAdminFromPark,
)

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>/advertisements', AutoParkAddAdvertisementView.as_view(), name='auto_parks_add_car'),

    path('/<int:pk>/usr_to_adm_prk', PromoteToAdminPark.as_view(), name='promote_to_admin_park'),
    path('/<int:pk>/usr_to_slsman_prk', PromoteToSalesmanPark.as_view(), name='promote_to_salesman_park'),
    path('/<int:pk>/usr_to_mech_prk', PromoteToMechanicPark.as_view(), name='promote_to_mechanic_park'),

    path('/<int:pk>/rm_adm_prk', RemoveAdminFromPark.as_view(), name='remove_from_admin_park'),
]
