from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.home, name='blog-home'),
    path('blog/blogs/', views.blog_list, name='blog-list'),
    path('blog/blogger/<int:author_id>/', views.author_detail, name='author-detail'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog-detail'),
    path('blog/bloggers/', views.blogger_list, name='blogger-list'),
    path('blog/<int:blog_id>/create/', views.create_comment, name='create-comment'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('custom_logout_page/', views.custom_logout_page, name='logout2'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('blog/create/', views.create_blog, name='create-blog'),
    path('accounts/signup/', views.signup, name='signup'),

]