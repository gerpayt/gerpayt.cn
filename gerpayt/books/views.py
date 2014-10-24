from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from models import BookTag, BookItem


def index(request):
    book_tag_list = BookTag.objects.all()
    book_item_list = BookItem.objects.all()
    context = {
        'book_tag_list': book_tag_list,
        'book_item_list': book_item_list,
    }
    return render(request, 'books/index.html', context)


def tag(request, tag_link):
    book_tag_list = BookTag.objects.all()
    book_tag = get_object_or_404(BookTag, link=tag_link)
    context = {
        'book_tag_list': book_tag_list,
        'book_tag': book_tag,
    }
    return render(request, 'books/tag.html', context)


def item(request, item_link):
    book_tag_list = BookTag.objects.all()
    book_item = get_object_or_404(BookItem, link=item_link)
    context = {
        'book_tag_list': book_tag_list,
        'book_item': book_item,
    }
    return render(request, 'books/item.html', context)


def search(request):
    book_tag_list = BookTag.objects.all()
    search_keyword = request.POST.get('keyword', '')
    book_item_list = BookItem.objects.filter(title__icontains=search_keyword)
    context = {
        'book_tag_list': book_tag_list,
        'book_item_list': book_item_list,
        'search_keyword': search_keyword,
    }
    return render(request, 'books/search.html', context)

