from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Article
from .forms import ArticleForm

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

def write(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArticleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_article = Article(author_name=form.cleaned_data['author_name'],
                                  title=form.cleaned_data['title'],
                                  article_text=form.cleaned_data['article_text'])
            new_article.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(f'/article-{new_article.id}')
        else:
            return HttpResponseRedirect('/write/fail')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArticleForm()

    return render(request, 'articles/write.html', {'form': form})
