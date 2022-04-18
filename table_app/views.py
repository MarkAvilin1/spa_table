from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import SortForm, FilterForm
from .filter_process import FilterProcess


def index(client):
    sorting = SortForm(client.GET)
    filters = FilterForm(client.GET)
    logic = FilterProcess(filters, sorting)
    result = logic.get_data
    page_no = client.GET.get('page_no', 1)
    paginator = Paginator(result, 5)
    page_obj = paginator.get_page(page_no)
    return render(client, 'index.html',
                  {'table': page_obj, "sorting": sorting, "filters": filters})


def httpResponse(client):
    sorting = SortForm(client.GET)
    filters = FilterForm(client.GET)
    logic = FilterProcess(filters, sorting)
    result = logic.get_data
    page_no = client.GET.get('page_no', 1)
    paginator = Paginator(result, 5)
    page_obj = paginator.get_page(page_no)
    serialize = serializers.get_serializer("python")()
    srlz_pages = serialize.serialize(page_obj.object_list,
                                     fields=('title', 'quantity', 'distance', 'date'))
    return JsonResponse(srlz_pages, safe=False)
