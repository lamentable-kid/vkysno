from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.blog.forms import CommentForm
from apps.blog.models import BlogCategory, Article, Tag, Commentariy
from config.settings import PAGE_NAMES


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {'current': PAGE_NAMES['blog']}
    return render(request, 'blog/category/list.html', {'categories': blog_categories, 'breadcrumbs': breadcrumbs})


def article_list(request, category_id):
    articles = Article.objects.filter(category=category_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog']}
    if category:
        breadcrumbs.update({'current': category})
    return render(request, 'blog/article/list.html', {'articles': articles, 'breadcrumbs': breadcrumbs})


def article_view(request, category_id, article_id):
    comments = Commentariy.objects.filter(article_connect=article_id)
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog']}
    error = None
    is_checked = False

    if request.method == 'POST':
        data = request.POST.copy()
        if request.user.is_authenticated:
            data.update(article_connect=article_id, username=request.user, email=request.user.email, is_checked=True)
        else:
            data.update(article_connect=article_id, is_checked=False)
        request.POST = data
        form = CommentForm(request.POST)
        if form.is_valid():
            breadcrumbs = {'current': 'Успешное добавление комментария'}
            form.save(commit=False)
            data.update(artid=article)
            form.save(data)
            return render(request, 'blog/success_page.html', {'breadcrumbs': breadcrumbs, 'next_page': request.path})
        else:
            error = form.errors
    else:
        form = CommentForm()

    if article:
        breadcrumbs.update({reverse('article_list', args=[category_id]): category})
    breadcrumbs.update({'current': article})
    return render(request, 'blog/article/view.html',
                  {'error': error, 'article': article, 'category': category,
                   'breadcrumbs': breadcrumbs, 'is_checked': is_checked, 'comments': comments})


def tag_view(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    # article_wh_ex_tag = Article.objects.filter(tags=tag_id) так тоже можно, но лучше способ снизу
    article_wh_ex_tag = Article.objects.filter(tags__in=[tag_id])
    breadcrumbs = {'current': PAGE_NAMES['blog']}
    if tag:
        breadcrumbs.update({reverse('tag_view', args=[tag_id]): tag})
    return render(request, 'blog/tag/list.html', {'article_wh_ex_tag': article_wh_ex_tag, 'breadcrumbs': breadcrumbs})