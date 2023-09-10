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


def recipe(request, recipe_name):
    """
    Общий обработчик, которые принимает параметр из URL'а
    :param request:
    :param recipe_name:
    :return:
    """
    try:
        servings = int(request.GET.get("servings"))
    except:
        servings = 1
    data = DATA[recipe_name]
    context = {"items": [[x, data[x] * servings] for x in data]}
    print(context)
    return render(request, 'calculator/index.html', context=context)


def omlet(request):
    try:
        servings = int(request.GET.get("servings"))
    except:
        servings = 1
    data = DATA["omlet"]
    context = {"items": [[x, data[x] * servings] for x in data]}
    print(context)
    return render(request, 'calculator/index.html', context=context)


def pasta(request):
    try:
        servings = int(request.GET.get("servings"))
    except:
        servings = 1
    data = DATA["pasta"]
    context = {"items": [[x, data[x] * servings] for x in data]}
    print(context)
    return render(request, 'calculator/index.html', context=context)


def buter(request):
    try:
        servings = int(request.GET.get("servings"))
    except:
        servings = 1
    data = DATA["buter"]
    context = {"items": [[x, data[x] * servings] for x in data]}
    print(context)
    return render(request, 'calculator/index.html', context=context)
