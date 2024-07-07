from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.dataclasses.auto_park_dataclass import AutoParkDataClass
from core.permissions.is_admin_park import IsAdminPark
from core.permissions.is_manager_or_admin import IsManagerOrAdminPark
from core.permissions.is_manager_park import IsManagerPark

from apps.advertisements.serializers import AdvertisementSerializer
from apps.auth.serializers import EmailSerializer
from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkWithOutCarsSerializer

UserModel = get_user_model()


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkWithOutCarsSerializer
    permission_classes = (IsAuthenticated,)


class AutoParkAddAdvertisementView(GenericAPIView):
    queryset = AutoParkModel.objects.all()
    permission_classes = (IsManagerOrAdminPark,)

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = AdvertisementSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        ap_serializer = AutoParkWithOutCarsSerializer(auto_park)
        return Response(ap_serializer.data, status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = AdvertisementSerializer(auto_park.advertisements, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class PromoteToAdminPark(GenericAPIView):
    serializer_class = EmailSerializer
    permission_classes = (IsManagerPark,)

    def post(self, request, pk):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        user = get_user_model()
        try:
            user = user.objects.get(email=email)
        except user.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            auto_park = AutoParkModel.objects.get(pk=pk)
        except AutoParkModel.DoesNotExist:
            return Response({"error": "Auto park not found"}, status=status.HTTP_404_NOT_FOUND)

        auto_park.admin = user
        auto_park.save()
        return Response({"message": "User promoted to admin successfully"}, status=status.HTTP_200_OK)


class PromoteToSalesmanPark(GenericAPIView):
    serializer_class = EmailSerializer
    permission_classes = (IsManagerOrAdminPark,)

    def post(self, request, pk):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        user = get_user_model()
        try:
            user = user.objects.get(email=email)
        except user.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            auto_park = AutoParkModel.objects.get(pk=pk)
        except AutoParkModel.DoesNotExist:
            return Response({"error": "Auto park not found"}, status=status.HTTP_404_NOT_FOUND)

        auto_park.salesperson = user
        auto_park.save()
        return Response({"message": "User promoted to admin successfully"}, status=status.HTTP_200_OK)


class PromoteToMechanicPark(GenericAPIView):
    serializer_class = EmailSerializer
    permission_classes = (IsManagerOrAdminPark,)

    def post(self, request, pk):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        user = get_user_model()
        try:
            user = user.objects.get(email=email)
        except user.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            auto_park: AutoParkDataClass = AutoParkModel.objects.get(pk=pk)
        except AutoParkModel.DoesNotExist:
            return Response({"error": "Auto park not found"}, status=status.HTTP_404_NOT_FOUND)

        auto_park.mechanic = user
        auto_park.save()
        return Response({"message": "User promoted to admin successfully"}, status=status.HTTP_200_OK)


class RemoveAdminFromPark(GenericAPIView):
    permission_classes = (IsManagerPark,)

    def delete(self, request, pk):
        try:
            auto_park = AutoParkModel.objects.get(pk=pk)
        except AutoParkModel.DoesNotExist:
            return Response({"error": "Auto park not found"}, status=status.HTTP_404_NOT_FOUND)

        if auto_park.admin_id is not None:
            auto_park.admin_id = None
            auto_park.save()
            return Response({"message": "Admin removed from park successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No admin assigned to this park"}, status=status.HTTP_400_BAD_REQUEST)
