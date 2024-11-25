from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('post/<slug:slug>',views.post_page,name='post_page'),
    path('tag/<slug:slug>',views.tag_page,name='tag_page'),
    path('author/<slug:slug>',views.author_page,name='author_page'),
    path('search/',views.search_posts,name='search'),
    path('about/',views.about,name='about'),
    path('accounts/register/',views.register_user,name='register'),
    path('bookmark_post/<slug:slug>',views.bookmark_post,name='bookmark_post'),
    path('like_post/<slug:slug>',views.like_post,name='like_post'),
]
