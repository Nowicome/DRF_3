from django_filters import rest_framework as filters

from advertisements.models import Advertisement


STATUS_CHOICES = (
    ("OPEN", "Открыто"),
    ("CLOSED", "Закрыто")
)


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFilter()
    status = filters.ChoiceFilter(choices=STATUS_CHOICES)
    creator = filters.DjangoFilterBackend()

    class Meta:
        model = Advertisement
        fields = ("created_at", "updated_at", "status", "creator")
