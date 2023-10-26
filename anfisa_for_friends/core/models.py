from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField(
        default=True,
        verbose_name = 'Опубликовано'
    ),
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        abstract = True

    # Настроим вывод записей так, чтобы 
    # в качестве заголовка показывалось название мороженого 
    # (значение поля title)
    def __str__(self):
        return self.title 
        
