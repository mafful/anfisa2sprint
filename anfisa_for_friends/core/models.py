from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет title & флаг is_published."""
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано')
    

    class Meta:
        abstract = True

    # Настроим вывод записей так, чтобы 
    # в качестве заголовка показывалось название мороженого 
    # (значение поля title)
    def __str__(self):
        return self.title 
   
        
