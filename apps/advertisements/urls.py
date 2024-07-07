from django.urls import path

from apps.advertisements.views import AdvertisementDetailView, AdvertisementListCreateView, UserAddAdvertisementView

urlpatterns = [
    path('', AdvertisementListCreateView.as_view(), name='advertisement_list_create'),
    path('/users', UserAddAdvertisementView.as_view(), name='users_add_car'),
    path('/<int:pk>/users/<int:advertisement_id>', UserAddAdvertisementView.as_view(),
         name='update_delete_advertisement'),
    path('/<int:pk>', AdvertisementDetailView.as_view(), name='advertisement_detail'),
]
