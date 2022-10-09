from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.blog.forms import CommentFormForRegistered, CommentFormForLogined
from apps.blog.models import BlogCategory, Article, Tag, Comment
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
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog']}
    if article:
        breadcrumbs.update({reverse('article_list', args=[category_id]): category})
    breadcrumbs.update({'current': article})
    return render(request, 'blog/article/view.html',
                  {'article': article, 'category': category, 'breadcrumbs': breadcrumbs})


def tag_view(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    # article_wh_ex_tag = Article.objects.filter(tags=tag_id) так тоже можно, но лучше способ снизу
    article_wh_ex_tag = Article.objects.filter(tags__in=[tag_id])
    breadcrumbs = {'current': PAGE_NAMES['blog']}
    if tag:
        breadcrumbs.update({reverse('tag_view', args=[tag_id]): tag})
    return render(request, 'blog/tag/list.html', {'article_wh_ex_tag': article_wh_ex_tag, 'breadcrumbs': breadcrumbs})


def comment_is_for_registered_applied(request):
    comments = Article.objects.get(comments=True)
    breadcrumbs = {}
    error = None
    next_page = request.GET.get('next', reverse('home'))
    if request.method == 'POST':
        form = CommentFormForRegistered(data=request.POST)
        if form.is_valid():
            breadcrumbs = {'current': 'Успешное добавление комментария'}
            comment = form.save(commit=True)
            HttpResponseRedirect(redirect_to=next_page)
            return render(request, 'blog/success_page.html', {'comment': comment, 'next_page': next_page,
                                                      'breadcrumbs': breadcrumbs})
        error = form.errors
    else:
        form = CommentFormForRegistered()
    return render(request, 'blog/article/view.html', {'comments': comments, 'error': error,
                                                  'breadcrumbs': breadcrumbs})


def comment_is_for_logined_applied(request):
    breadcrumbs = {}
    error = None
    next_page = request.GET.get('next', reverse('home'))
    if request.method == 'POST':
        form = CommentFormForLogined(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'], email=cleaned_data['email'])
            if user:
                breadcrumbs = {'current': 'Успешное добавление комментария'}
                return render(request, 'blog/article/view.html', {'request': request, 'next_page': next_page,
                                                                  'breadcrumbs': breadcrumbs})
    else:
        form = CommentFormForLogined()
    return render(request, 'user/login.html', {'form': form, 'error': error, 'breadcrumbs': breadcrumbs})
