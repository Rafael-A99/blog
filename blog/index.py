import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Post, Comment

@register(Post)
class PostIndex(AlgoliaIndex):
    fields = ('title', 'content')  
    settings = {'searchableAttributes': ['title']}
    index_name = 'blog_posts'

@register(Comment)
class CommentIndex(AlgoliaIndex):
    fields = ('content',)  
    settings = {'searchableAttributes': ['content']}
    