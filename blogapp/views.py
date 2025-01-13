from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from .form import BlogForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    posts_list = Post.objects.all().order_by('-date_posted')
    page = request.GET.get('page', 1)
    
    paginator = Paginator(posts_list, 3)
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blogs/homepage.html',{'posts':posts})

def about(request):
    return render(request, 'blogs/aboutpage.html')

@login_required
def userblogs(request):
    
    posts= Post.objects.filter(auther=request.user).order_by('-date_posted')
    return render(request, 'blogs/userblogs.html', {'posts':posts})


@login_required
def create_blog(request):
    
    if request.method == 'POST':
        
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.auther = request.user  
            blog.save()
            return redirect('blog-userblogs')  
    else:
        form = BlogForm()

    return render(request, 'blogs/create_blog.html', {'form': form})


@login_required
def update_blog(request, pk):
    
    blog = get_object_or_404(Post, pk=pk, auther=request.user)

    if request.method == 'POST':
        
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog-userblogs') 
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'blogs/update_blog.html', {'form': form})

@login_required
def delete_blog(request, pk):
    
    blog = get_object_or_404(Post, pk=pk, auther=request.user) 
    blog.delete() 
    return redirect('blog-userblogs') 