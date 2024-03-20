from django.urls import path, include
from djoser import views as djoser_views
from .views import index_view, PostViewSet, CommentViewSet, search_view

urlpatterns = [
    path('', index_view, name='index'),
    path('search/', search_view, name='search'),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post'),
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment'),
    path('auth/', djoser_views.TokenCreateView.as_view(), name='login'),

    ]
