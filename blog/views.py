from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK , HTTP_201_CREATED ,HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated,BasePermission,SAFE_METHODS


from .models import Blog,Comment
from .serializers import BlogSerializers,CommentSerializers
from permissions import IsOwnerOrReadOnly
# Create your views here.
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.methods in SAFE_METHODS


class ListViewsBlog(APIView):
    def get(self,request):
        blogs = Blog.objects.all()
        ser_data = BlogSerializers(instance=blogs ,many=True)
        return Response(ser_data.data , status=HTTP_200_OK)


class CreateViewBlog(APIView):
    serializer_class = BlogSerializers
    def post(self,request):
        ser_data = BlogSerializers( data = request.POST)
        if ser_data.is_valid():
            Blog.objects.create(
                user = ser_data.validated_data['user'],
                title = ser_data.validated_data['title'],
                body = ser_data.validated_data['body'],
                choices_wishlist = ser_data.validated_data['choices_wishlist'],
            )
            return Response(data = ser_data.data , status=HTTP_201_CREATED)

        return Response(ser_data.errors , status=HTTP_400_BAD_REQUEST)




class UpdateViewBlog(APIView):
    def put(self,request ,pk):
        blog = Blog.objects.get(pk=pk)
        # self.check_permissions(request , blog)
        ser_data = BlogSerializers(instance=blog , data = request.data , partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data , status=HTTP_200_OK)

        return Response(ser_data.errors , status=HTTP_400_BAD_REQUEST)



class DeleteViewsBlog(APIView):
    def delete(self,request,pk):
        blog = Blog.objects.get(pk=pk)
        ser_data = BlogSerializers(instance=blog ,data = request.data, partial=True)
        if ser_data.is_valid():
            blog.delete()
            return Response({'massage':'your blog was deleted'} , status=HTTP_200_OK)

        return Response(ser_data.errors , status=HTTP_400_BAD_REQUEST)


#Comments Views-------------------------------------

class ListCommentViews(APIView):
    def get(self,request):
        comments = Comment.objects.all()
        ser_data  = CommentSerializers(instance=comments , many=True)
        return Response(data = ser_data.data)



class CreateComment(APIView):
    def post(self,request):
        ser_data = CommentSerializers(data = request.POST , partial=True)
        if ser_data.is_valid():
            Comment.objects.create(
                user = ser_data.validated_data['user'],
                blog = ser_data.validated_data['blog'],
                text = ser_data.validated_data['text'],
                choices_wishlist= ser_data.validated_data['choices_wishlist'],
            )
            return Response(ser_data.data ,status= HTTP_201_CREATED )

        return Response(ser_data.errors ,status=HTTP_400_BAD_REQUEST)




class UpdateCommentViews(APIView):

    def put(self,request,pk):
        comment = Comment.objects.get(pk=pk)
        ser_data = CommentSerializers(instance= comment , data = request.POST , partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=HTTP_200_OK)

        return Response(ser_data.errors , status=HTTP_400_BAD_REQUEST)



class DeleteCommentViews(APIView):

    def delete(self,request,pk):
        comment = Comment.objects.get(pk=pk)
        ser_data = CommentSerializers(instance=comment , data = request.data)
        if ser_data.is_valid():
            comment.delete()
            return Response({'massage':'Your comment was deleted'})
