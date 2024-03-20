from django.http import HttpResponseForbidden
from .models import Post, Comment

class AuthorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            # Verificar si es un post
            post_id = view_kwargs.get('post_id')
            if post_id:
                try:
                    post = Post.objects.get(id=post_id)
                    if post.author != request.user:
                        return HttpResponseForbidden("No tienes permiso para modificar este post.")
                except Post.DoesNotExist:
                    pass

            # Verificar si es un comentario
            comment_id = view_kwargs.get('comment_id')
            if comment_id:
                try:
                    comment = Comment.objects.get(id=comment_id)
                    if comment.author != request.user:
                        return HttpResponseForbidden("No tienes permiso para modificar este comentario.")
                except Comment.DoesNotExist:
                    pass

        return None