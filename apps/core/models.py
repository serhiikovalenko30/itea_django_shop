from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    """
        Класс описывает таблицу и поля в базе данных для сущности Category
    """
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'категория'  # отображение названия модели в админке
        verbose_name_plural = 'категории'  # во множественном числе
        ordering = ('title',)  # сортировка по title (в алфавитном порядке)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
        Класс описывает таблицу и поля в базе данных для сущности Product
    """
    title = models.CharField(
        verbose_name='название',
        max_length=255,
        help_text='Максимальная длина 255 символов',
    )
    category = models.ForeignKey(
        Category,
        verbose_name='категория',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name='теги',
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    image = models.ImageField(
        verbose_name='изображение',
        upload_to='product',
        blank=True,
        null=True,
    )
    price = models.FloatField(
        verbose_name='цена',
    )
    discount = models.FloatField(
        verbose_name='скидка',
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0)
        ],
        default=0,
    )
    bonus = models.PositiveIntegerField(
        verbose_name='бонус',
        default=1,
    )
    in_stock = models.BooleanField(
        verbose_name='в наличии?',
        default=True,
    )

    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='дата последнего изменения',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('-pk',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # здесь описываем логику до сохранения объекта
        super().save(*args, **kwargs)
        # здесь описываем логику после сохранения объекта
