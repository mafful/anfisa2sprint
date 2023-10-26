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

    class Meta:
        verbose_name = 'обертка'
        verbose_name_plural = 'Обертки' 


class IceCream(PublishedModel):
    description = models.TextField(verbose_name='Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name = 'обертка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='категория'
    )
    toppings = models.ManyToManyField(Topping, verbose_name='слаг')
    is_on_main = models.BooleanField(
        default=False,
        verbose_name='На главную'
    )

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'Мороженое' 

