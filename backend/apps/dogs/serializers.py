from rest_framework import serializers
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    """Сериализатор модели породы."""

    dog_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = "__all__"


class DogSerializer(serializers.ModelSerializer):
    """Сериализатор модели собаки.

    Включает вложенную информацию о породе и средний возраст собак этой породы.
    """

    breed_info = BreedSerializer(source="breed", read_only=True)
    same_breed_count = serializers.IntegerField(read_only=True)
    average_age_for_breed = serializers.FloatField(read_only=True)

    class Meta:
        model = Dog
        fields = "__all__"
