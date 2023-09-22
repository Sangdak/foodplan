from django.shortcuts import render
from .models import Culinary, Term, Allergen


def user_profile(request):
    context = {
        'user_info': request.user,
    }
    return render(request, 'lk.html', context)


def order_page(request):
    culinarys = Culinary.objects.all()
    count = culinarys.count()
    titles_culinary = ''
    for index, item in enumerate(culinarys):
        if index == count-1:
            titles_culinary += ' и '
        elif index != 0:
            titles_culinary += ', '
        titles_culinary += item.title
    titles_culinary += '.'

    culinary = {
        'count_culinary': count,
        'titles_culinary': titles_culinary
        }

    terms = Term.objects.all()
    term = []
    for index, item in enumerate(terms):
        print(index, item)
        if index == 0:
            selected = 'selected'
        else:
            selected = ''
        term.append({'index': str(index),
                     'selected': selected,
                     'title': item.title})

    allergens = Allergen.objects.all()
    allergen = []
    for index, item in enumerate(allergens):
        allergen.append({'index': str(index + 1),
                         'title': item.title})

    print('allergen', allergen)
    context = {
        'culinary': culinary,
        'terms': term,
        'allergens': allergen}

    return render(request, 'order.html', context)
