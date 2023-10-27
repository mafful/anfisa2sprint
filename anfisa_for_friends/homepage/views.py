# Для применения Q-объектов их нужно импортировать:
from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    
    ''' 
    Заключаем вызов методов в скобки
    (это стандартный способ переноса длинных строк в Python);
    каждый вызов пишем с новой строки, так проще читать код:
    '''
    # ice_cream_list = IceCream.objects.values(
    #         'id', 'title', 'description'
    #     # Верни только те объекты, у которых в поле is_on_main указано True:
    #     ).filter(
    #     # Делаем запрос, объединяя два условия
    #     # через Q-объекты и оператор AND:
    #     (Q(is_on_main=True) & Q(is_published=True)) |
    #      (Q(title__contains='пломбир') & Q(is_published=True))
    # ).order_by('title')[0:4] 


    '''
    В аргументе метода .values() передаётся имя атрибута,
    где хранится внешний ключ (category в приведённом примере), 
    и через двойное нижнее подчёркивание — название того поля 
    связанной модели, значение которого нужно получить.
    '''
    # ice_cream_list = IceCream.objects.select_related(
    #     'category').filter(
    #         is_published=True,
    #         is_on_main=True
    # ).order_by('title')[0:4]

    # Запрашиваем нужные поля из базы данных:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        # Проверяем, что
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации.
    )

    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context) 