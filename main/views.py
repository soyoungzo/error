from django.shortcuts import render, get_object_or_404, redirect
#장고에만 있는 기능, get_object_or 404 정보가 없으면 나타나게 하는 페이지(페이지낫파운드)
from .models import Blog
from django.utils import timezone
from login.models import Account

def main(request):
    blog = Blog.objects
    text = ""
    if request.user.is_authenticated:
        txt_prime = Account.objects.get(user=request.user)
        text = txt_prime.nickname + "님 안녕하세요!"
    else:
        text = "로그인해주세요"
    #now_login = Account.objects.get(user = request.user)
    #context = {'blog':blog, 'user':now_login}
    return render(request, 'main.html', {'blog':blog, 'txt':text})

def other(request):
    return render(request,'other.html')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def news(request):
    return render(request, 'news.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))
    #redirect는 return값을 url로 이동해서 보여줌

def delete(request):
    del_id = request.GET['blogNum']
    #GET은 정보를 보내주는(생성해주는)
    blog = Blog.objects.get(id=del_id)
    blog.delete()
    return redirect('http://127.0.0.1:8000/')

def port(request):
    return render(request, 'portfolio.html')
# Create your views here.
