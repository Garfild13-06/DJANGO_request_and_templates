from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def test(request):
    name = request.GET.get("name")
    age = int(request.GET.get("age", 20))
    return HttpResponse(f'{name=} {age=}')


def summ(request, a, b):
    result = a + b
    return HttpResponse(f'Sum = {result}')


def omlet(request):
    items=DATA["omlet"]
    return render(request, 'calculator/index.html')
    # return HttpResponse(items)


def pasta(request):
    return HttpResponse('Hello from django')


def buter(request):
    return HttpResponse('Hello from django')

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
