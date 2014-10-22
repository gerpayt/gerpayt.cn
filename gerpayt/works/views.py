from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse

from models import WorkCate, WorkItem


def index(request):
    work_cate_list = WorkCate.objects.order_by('sort')
    context = {
        'work_cate_list': work_cate_list,
    }
    return render(request, 'index.html', context)


def cate(request, cate_link):
    work_cate = get_object_or_404(WorkCate, link=cate_link)
    context = {
        'work_cate': work_cate,
    }
    return render(request, 'cate.html', context)


def item(request, item_link):
    work_item = get_object_or_404(WorkItem, link=item_link)
    context = {
        'work_item': work_item,
    }
    return render(request, 'item.html', context)
