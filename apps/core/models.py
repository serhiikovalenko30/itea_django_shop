from django.db import models
from django.core.validators import MaxValueValidator


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255,
        help_text='Максимальная длина 254 символа',
        unique_for_date='date',
        error_messages={'unique_for_date': 'some error'}
    )
    description = models.TextField(verbose_name='Описание', blank=True)
    email = models.EmailField()
    url = models.URLField()
    bonus = models.IntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(100)]
    )
    bonus_positive = models.PositiveIntegerField(default=1)
    price = models.FloatField()
    active = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    date = models.DateTimeField()

    test_file = models.FileField(upload_to='product')

    COLOR_CHOICES = (
        ('b', 'black'),
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

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag)
    # description = models.TextField('Описание')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
