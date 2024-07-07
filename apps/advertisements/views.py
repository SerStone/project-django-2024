from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.advertisements.models import AdvertisementModel
from apps.advertisements.serializers import AdvertisementSerializer, PremiumAdvertisementSerializer
from apps.users.serializers import UserSerializer

from .utils import get_exchange_rates

UserModel = get_user_model()


class AdvertisementListCreateView(ListAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (IsAuthenticated,)


class UserAddAdvertisementView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_user(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        user = self.get_user()
        data = request.data

        if not user.is_premium and user.advertisements.count() >= 1:
            return Response(
                {"detail": "Basic account can only have one advertisement."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = AdvertisementSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user.is_seller = True
        user.save()
        serializer.save(user=user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        user = self.get_user()
        serializer = AdvertisementSerializer(user.advertisements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = self.get_user()
        advertisement_id = kwargs.get('advertisement_id')
        advertisement = get_object_or_404(AdvertisementModel, id=advertisement_id, user=user)

        data = request.data
        serializer = AdvertisementSerializer(advertisement, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user = self.get_user()
        advertisement_id = kwargs.get('advertisement_id')
        advertisement = get_object_or_404(AdvertisementModel, id=advertisement_id, user=user)

        advertisement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdvertisementDetailView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = AdvertisementModel.objects.all()

    def get_serializer_class(self):
        advertisement = self.get_object()
        user = self.request.user
        if user.is_premium and advertisement.user == user:
            return PremiumAdvertisementSerializer
        else:
            return AdvertisementSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        advertisement = self.get_object()
        advertisement.increment_view_count()

        get_exchange_rates()

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(advertisement)
        return Response({
            'advertisement': serializer.data
        }, status=status.HTTP_200_OK)
