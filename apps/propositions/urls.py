from django.urls import path

from .views import PropositionDetailView, PropositionListCreateView

urlpatterns = [
    path('', PropositionListCreateView.as_view(), name='proposition-list-create'),
    path('/<int:pk>/', PropositionDetailView.as_view(), name='proposition-detail'),
]