from random import random
from django.shortcuts import render
from . import min_max_heap
import random
from .models import Districts


def index(request):
    return render(request, 'index.html')


def show_vaxx(request):
    vaccinated_data = []
    districts = Districts.objects.all().values(
        'vaccinated', 'name')
    # print(f'Districts_all:{districts}')
    for i in districts:
        if i['vaccinated']:
            vaccinated_data.append(i['vaccinated'])
    print(vaccinated_data)
    max = min_max_heap.max_heap(vaccinated_data)
    min = min_max_heap.min_heap(vaccinated_data)
    district_with_max = Districts.objects.get(vaccinated=max)
    district_with_min = Districts.objects.get(vaccinated=min)

    context = {'district_with_max': district_with_max,
               'district_with_min': district_with_min, }

    if request.GET:
        context['districts'] = districts
    return render(request, 'show_cases.html', context)
