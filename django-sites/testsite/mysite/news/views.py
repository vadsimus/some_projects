from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'список новостей'
    }
    return render(request, 'news/index.html', context)


def test(request):
    return HttpResponse('<h1>тестовая страница</h1>')


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})
