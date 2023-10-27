from django.shortcuts import get_object_or_404, render

from ice_cream.models import IceCream

def ice_cream_detail(request, pk):
    template_name = 'ice_cream/detail.html'
    # Из модели IceCream получаем QuerySet, содержащий только
    # поля 'title' и 'description' всех записей.
    # Из этого QuerySet получаем запись, 
    # у которой значение поля pk равно значению пременной pk, 
    # полученной в аргументе view-функции.
    # Если объекта с указанным pk не существует - вернётся страница с ошибкой 404:
    ice_cream = get_object_or_404(
        IceCream.objects.select_related('wrapper')
        .filter(is_published=True, category__is_published=True),
        pk=pk
    )
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template_name, context) 



def ice_cream_list(request):
    template = 'ice_cream/list.html'
    ice_cream_list = get_object_or_404(
        IceCream.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True
    ).order_by('category')
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
