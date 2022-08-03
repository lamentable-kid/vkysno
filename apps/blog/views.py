from django.shortcuts import render
from apps.blog.models import BlogCategory, Article, Tag


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    return render(request, 'blog/category/list.html', {'categories': blog_categories})


def article_list(request, category_id):
    articles = Article.objects.filter(category=category_id)
    return render(request, 'blog/article/list.html', {'articles': articles})


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/article/view.html', {'article': article, 'category': category})


def tag_view(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    # article_wh_ex_tag = Article.objects.filter(tags=tag_id) так тоже можно, но лучше способ снизу
    article_wh_ex_tag = Article.objects.filter(tags__in=[tag_id])
    return render(request, 'blog/tag/list.html', {'article_wh_ex_tag': article_wh_ex_tag, 'tag': tag})
