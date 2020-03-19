from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BlogSerializer


@api_view(['GET', ])
def api_detail_blog_view(request, slug):
    blog_post = BlogPost.objects.get(slug=slug)
    if (request.method == 'GET'):
        serializer = BlogSerializer(blog_post)
        return Response(serializer.data)

