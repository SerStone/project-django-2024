from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED

from .models import PropositionModel
from .serializers import PropositionSerializer


class PropositionListCreateView(generics.ListCreateAPIView):
    queryset = PropositionModel.objects.all()
    serializer_class = PropositionSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            data={"detail": ("Your proposition is under review.")},
            status=HTTP_202_ACCEPTED,
            headers=headers
        )


class PropositionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropositionModel.objects.all()
    serializer_class = PropositionSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
