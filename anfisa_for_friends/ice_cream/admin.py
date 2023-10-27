from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, Topping, Wrapper, IceCream

# Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin):
    # В этом классе опишем все настройки, какие захотим.
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
     
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    

    search_fields = ('title',) 
    list_filter = ('is_published','category')
    list_display_links = ('title',)
    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)

    # Это свойство сработает для всех полей этой модели.
    # Вместо пустого значения будет выводиться строка "Не задано".
    empty_value_display = 'Не задано'


# ...и регистрируем её в админке:
admin.site.register(IceCream, IceCreamAdmin)

# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )

# ...и регистрируем её в админке:
admin.site.register(Category, CategoryAdmin)

# ...и регистрируем их в админке:
admin.site.register(Topping) 
admin.site.register(Wrapper) 
