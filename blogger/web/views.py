from django.shortcuts import render, reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from users.models import Author
from web.models import Category, Blog, Tag


def index(request):
    categories = Category.objects.all()
    blogs = Blog.objects.all()

    authors = Author.objects.all()
    tags = Tag.objects.all()

    context = {
        "categories": categories,
        "blogs": blogs,
        "authors": authors,
        "tags": tags,
    }
    return render(request, 'web/index.html', context=context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            auth_login(request, user)

            return HttpResponseRedirect(reverse('web:index'))
        
        else:
            return render(request, 'web/login.html')
    
    else:
        return render(request, 'web/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password

        )

        user.save()


        author = Author.objects.create(
            user=user,
        )

        author.save()

        return HttpResponseRedirect(reverse('web:login'))
    else:
        return render(request, 'web/register.html')


def logout(request):
    user = request.user
    auth_logout(request)

    return HttpResponseRedirect(reverse('web:index'))


@login_required(login_url='/login')
def create(request):
    user = request.user
    author = Author.objects.get(user=user)
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        short_description = request.POST.get('short_description')
        description = request.POST.get('description')
        category = request.POST.get('category')

        category = Category.objects.get(id=category)

        blog = Blog.objects.create(
            title=title,
            description=description,
            category=category,
            short_description=short_description,
            image=image,
            author=author
         )
        blog.save()
        
        return HttpResponseRedirect(reverse('web:index'))

    else:


        context = {
            "categories": categories
        }

        return render(request, 'web/create.html', context=context)


def blog(request, id):
    blog = Blog.objects.get(id=id)
    blogs = Blog.objects.all()[:5]

    context = {
            "blog": blog,
            "blogs": blogs
    }
    return render(request, 'web/blog.html', context=context)


@login_required(login_url='/login')
def account(request):
    user = request.user
    author = Author.objects.get(user=user)

    blogs = Blog.objects.filter(author=author)

    context = {
           "blogs":blogs, 
    }
    return render(request, 'web/account.html', context=context)



login_required(login_url='/login')
def blog_delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()

    return HttpResponseRedirect(reverse('web:index'))

