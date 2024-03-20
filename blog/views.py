from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from django.contrib.auth.models import User
from .serializer import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from algoliasearch_django import raw_search
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from functools import wraps
from django.core.mail import EmailMessage
from django.http import HttpResponse

def token_authentication_middleware(get_response):
    @wraps(get_response)
    def middleware(request):
        # Verificar si se proporciona un token en el encabezado de autorización
        if 'HTTP_AUTHORIZATION' in request.META:
            try:
                token_key = request.META['HTTP_AUTHORIZATION'].split()[1]
                token = Token.objects.get(key=token_key)
                # Autenticar al usuario utilizando el token
                request.user = token.user
            except Token.DoesNotExist:
                return JsonResponse({'error': 'Token inválido'}, status=401)

        response = get_response(request)
        return response

    return middleware

def search_view(request):
    query = request.GET.get('q', '')
    results = raw_search('blog_posts', query)  
    return render(request, 'index.html', {'results': results, 'query': query})

def index_view(request):
    template_name = "index.html"
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, template_name, context)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

def enviar_correo(request):
    if request.method == 'POST':
        
        asunto = request.POST['asunto']
        cuerpo = request.POST['cuerpo']
        remitente = request.POST['remitente']
        destinatario = request.POST['destinatario']

        email = EmailMessage(
            asunto,
            cuerpo,
            remitente,
            [destinatario],
        )
        email.send()

        return HttpResponse('Correo enviado')

    