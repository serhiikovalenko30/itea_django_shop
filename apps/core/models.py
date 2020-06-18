from django.db import models
from django.core.validators import MaxValueValidator


class Category(models.Model):
    """
        Класс описывает таблицу и поля в базе данных для сущности Category
    """
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'category'  # отображение названия модели в админке
        verbose_name_plural = 'categories'  # во множественном числе
        ordering = ('title',)  # сортировка по title (в алфавитном порядке)

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
        Класс описывает таблицу и поля в базе данных для сущности Tag
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
        Класс описывает таблицу и поля в базе данных для сущности Product
    """
    title = models.CharField(
        verbose_name='Название',
        max_length=255,
        help_text='Максимальная длина 255 символов',
        unique_for_date='date',  # пара значений полей title и date должна быть уникальной
        error_messages={'unique_for_date': 'some error'}
    )
    description = models.TextField(verbose_name='Описание', blank=True)
    email = models.EmailField()
    url = models.URLField()
    bonus = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(100)]
    )
    price = models.FloatField()
    active = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    date = models.DateTimeField()

    test_file = models.FileField(upload_to='product')

    COLOR_CHOICES = (
        ('b', 'black'),  # 'b' - записывается в БД, 'black' - отображается в админке
        ('w', 'white'),
        ('r', 'red')
    )

    COLOR_INT_CHOICES = (
        (0, 'black'),
        (1, 'white'),
        (2, 'red')
    )

    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='b')
    color_int = models.IntegerField(choices=COLOR_INT_CHOICES, default=0)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  # (при удалении Category - удаляются все связанные Product)
        null=True,
        related_name='products'  # ключ, по которому можно взять связанные Product из Category (category_obj.products.all())
    )
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(blank=True, null=True, upload_to='product')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # здесь описываем логику до сохранения объекта
        super().save(*args, **kwargs)
        # здесь описываем логику после сохранения объекта
