from . import views
from django.urls import path


# URL patterns for the blog app
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('search/<str:search_term>', views.search_post, name='search'),
    path('search.html', views.search_post, name='search_post'),
    path('about.html', views.about, name='about'),
    path('bookmarks.html', views.bookmark_list, name='view_bookmarks'),
    path('bookmark/<slug:slug>', views.PostBookmark.as_view(), name=' \
        post_bookmarks'),
]
