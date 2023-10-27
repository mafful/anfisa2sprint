from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    slug = models.SlugField(
        max_length=64, 
        unique=True,
        verbose_name='Слаг'
    )
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
        )
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории' 
    
    
class Topping(PublishedModel):
    slug = models.SlugField(
        max_length=64, 
        unique=True,
        verbose_name='Слаг'
    )

    class Meta:
            verbose_name = 'топпинг'
            verbose_name_plural = 'Топпинги' 
    

class Wrapper(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название обёртки, не более 256 символов'
    )
    class Meta:
        verbose_name = 'Обёртка'
        verbose_name_plural = 'Обёртки' 
    

class IceCream(PublishedModel):
    is_on_main = models.BooleanField(
        default=False,
        verbose_name='На главную'
    )
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
    )
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name = 'Обёртка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(
        Topping, 
        verbose_name = 'Топпинги'
    )
    
    

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'Мороженое' 
        # Сначала сортируем по полю output_order, 
        # а если у нескольких объектов значения output_order совпадают-- 
        # сортируем по title.
        ordering = ('output_order', 'title')


