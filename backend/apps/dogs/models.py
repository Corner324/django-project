from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Breed(models.Model):

    class BreedSize(models.TextChoices):
        TINY = "Tiny", "Tiny"
        SMALL = "Small", "Small"
        MEDIUM = "Medium", "Medium"
        LARGE = "Large", "Large"

    name = models.CharField(max_length=20)
    breedSize = models.CharField(
        max_length=7,
        choices=BreedSize.choices,
        default=BreedSize.MEDIUM,
        verbose_name="Размер",
    )

    friendliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Дружелюбие",
    )
    trainability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Обучаемость",
    )
    shedding_amount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Интенсивность линьки",
    )
    exercise_needs = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Потребность в активности",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dog(models.Model):

    class DogGender(models.TextChoices):
        MALE = "самец", "самец"
        FEMALE = "самка", "самка"

    name = models.CharField(max_length=20, verbose_name="Имя")
    age = models.IntegerField(verbose_name="Возраст")
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name="Порода")
    gender = models.CharField(
        max_length=6,
        choices=DogGender.choices,
        default=DogGender.MALE,
        verbose_name="Пол",
    )
    color = models.CharField(max_length=20, verbose_name="Цвет")
    favorite_food = models.CharField(max_length=20, verbose_name="Любимая еда")
    favorite_toy = models.CharField(max_length=20, verbose_name="Любимая игрушка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
