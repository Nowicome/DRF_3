from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""

        # if self.action in ["create", "update", "partial_update", "destroy"]:
        #     return [IsAuthenticated(), IsOwner()]
        #     # permission_classes = [IsAuthenticated, IsOwner]
        #     # return [permission() for permission in permission_classes]
        # return []

        if self.action in ("create", "update", "partial_update", "destroy"):
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super(self.__class__, self).get_permissions()
