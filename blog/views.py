from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Blog
from django.urls import reverse

def index(request):
    latest_blog = Blog.objects.order_by('-pub_date')[:5]
    return render(request, 'list.html', {'latest_blog': latest_blog})



def detail(request, blog_id):
    try:
        a = Blog.objects.get(id = blog_id)
    except:
        raise Http404('Статья не найдена!')

    latest_comments = a.comment_set.order_by('-id')[:10]

    return render(request, 'detail.html', {'blog': a, 'latest_comments': latest_comments})



def leave_comment(request, blog_id):
    try:
        a = Blog.objects.get(id = blog_id)
    except:
        raise Http404('Статья не найдена!')

    a.comment_set.create(author_name = request.POST['name'], text = request.POST['text'])

    return HttpResponseRedirect(reverse('blog:detail', args=(a.id, )))