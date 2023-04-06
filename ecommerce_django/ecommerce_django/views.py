
from django.shortcuts import render
# from app.models import Category


def index(request):
    # category = Category.objects.all()

    # context = {
    #     'category': category
    # }
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')
