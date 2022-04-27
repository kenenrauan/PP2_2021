from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Post, Category


# Create your views here.
from .serializers import PostSerializer


def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def postDetail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "DELETE":
        post.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


def postLike(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    post.like_cnt += 1
    post.save()
    serializer = PostSerializer(post)
    return JsonResponse(serializer.data, safe=False)


def postsByCats(request, id):
    posts = Post.objects.filter(category_id=id)
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)