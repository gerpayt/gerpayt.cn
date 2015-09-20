from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse


def index(request):

    return render(request, 'resume/index.html')

