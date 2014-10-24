from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from models import WorkCate, WorkItem


def index(request):
    work_cate_list = WorkCate.objects.all()
    context = {
        'work_cate_list': work_cate_list,
    }
    return render(request, 'works/index.html', context)


def cate(request, cate_link):
    work_cate = get_object_or_404(WorkCate, link=cate_link)
    context = {
        'work_cate': work_cate,
    }
    return render(request, 'works/cate.html', context)


def item(request, item_link):
    work_item = get_object_or_404(WorkItem, link=item_link)
    context = {
        'work_item': work_item,
    }
    return render(request, 'works/item.html', context)
