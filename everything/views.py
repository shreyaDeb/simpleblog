from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .models import Blogger
from .models import BlogPost
from .forms import CommentForm
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'home.html')


def blog_list(request):
    blog_posts = BlogPost.objects.order_by('-post_date')
    paginator = Paginator(blog_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'page_obj': page_obj})

def author_detail(request, author_id):
    author = get_object_or_404(Blogger, pk=author_id)
    blog_posts = author.blogpost_set.order_by('-post_date')
    return render(request, 'author_detail.html', {'author': author, 'blog_posts': blog_posts})

def blog_detail(request, blog_id):
    blog_post = get_object_or_404(BlogPost, pk=blog_id)
    comments = blog_post.comment_set.order_by('post_date')
    return render(request, 'blog_detail.html', {'blog_post': blog_post, 'comments': comments})

def blogger_list(request):
    bloggers = Blogger.objects.all()
    return render(request, 'blogger_list.html', {'bloggers': bloggers})

def create_comment(request, blog_id):
    blog_post = get_object_or_404(BlogPost, pk=blog_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = blog_post
            comment.save()
            return redirect('blog-detail', blog_id=blog_id)
    else:
        form = CommentForm()

    return render(request, 'comment_form.html', {'form': form, 'blog_post': blog_post})

def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user.blogger  # Assuming you have a Blogger profile associated with the logged-in user
            new_blog.save()
            return redirect('blog-list')  # Redirect to the list of blogs
    else:
        form = BlogPostForm()

    return render(request, 'create_blog.html', {'form': form})


@login_required
def my_profile(request):
    blogger = Blogger.objects.get(user=request.user)
    return render(request, 'my_profile.html', {'blogger': blogger})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            login(request, user)
            return redirect('home')  # Redirect to the homepage or any other desired page.
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

