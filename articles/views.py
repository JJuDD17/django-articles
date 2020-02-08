from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Article

def index(request):
    latest_articles_list = Article.objects.order_by('-publish_date')
    template = loader.get_template('articles/index.html')
    context = {
        'latest_articles_list': latest_articles_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail.html', {'article': article})

def write(resuest):
    return HttpResponse('write')
