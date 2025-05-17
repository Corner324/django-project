from rest_framework import viewsets
from django.db.models import Count, Avg, Subquery, OuterRef
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    """Вьюсет для управления собаками.

    Подставляет в сериализатор:
    - Средний возраст всех собак данной породы.
    - Количество собак той же породы.
    """

    def get_queryset(self):
        """Возвращает queryset с аннотациями.

        Returns:
            QuerySet: Queryset собак с аннотированными значениями.
        """
        breed_avg_age = (
            Dog.objects.filter(breed=OuterRef("breed")).values("breed").annotate(avg_age=Avg("age")).values("avg_age")
        )

        same_breed_count = (
            Dog.objects.filter(breed=OuterRef("breed")).values("breed").annotate(count=Count("id")).values("count")
        )

        return Dog.objects.annotate(
            average_age_for_breed=Subquery(breed_avg_age),
            same_breed_count=Subquery(same_breed_count),
        )

    serializer_class = DogSerializer


class BreedViewSet(viewsets.ModelViewSet):
    """Вьюсет для управления породами.

    Подставляет в сериализатор количество собак каждой породы.
    """

    queryset = Breed.objects.annotate(dog_count=Count("dog"))
    serializer_class = BreedSerializer
