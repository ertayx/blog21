from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post

@api_view(['GET'])
def posts_list(request):
    queryset = Post.objects.all()
    serialiser = PostSerializer(queryset, many = True)
    return Response(serialiser.data)

