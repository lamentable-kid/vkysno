from django.shortcuts import render
from django.urls import reverse

from apps.blog.models import BlogCategory, Article, Tag
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
