from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegisterSerializers,UserSerializers


# Create your views here.



class UserRegisterView(APIView):

    def post(self,request):
        ser_data = UserRegisterSerializers( data =request.POST)
        if ser_data.is_valid():
            User.objects.create_user(
                username = ser_data.validated_data['username'],
                email = ser_data.validated_data['email'],
                password = ser_data.validated_data['password'],
            )

            return Response(ser_data.data ,status=HTTP_200_OK)

        return Response(ser_data.errors , status=HTTP_400_BAD_REQUEST)



#
# class UserViewSet(viewsets.ViewSet):
#     queryset = User.objects.all()
#
#     def list(self,request):
#         ser_data = UserSerializers(instance=self.queryset , many=True)
#         return Response(ser_data.data , status= HTTP_200_OK)
#
#     def retrieve(self,request , pk=None):
#         user = get_object_or_404(User , pk=pk)
#         ser_data = UserSerializers(instance=user)
#         return Response(data = ser_data.data ,status=HTTP_200_OK)
#
#
#     def partial_update(self,request,pk):
#         user = get_object_or_404(User ,pk=pk)
#         ser_data = UserSerializers(instance=User , data = request.data , partial=True)
#         if ser_data.is_valid():
#             ser_data.save()
#             return Response(ser_data.data , status=HTTP_200_OK)
#
#         return Response(ser_data.errors , status=HTTP_400_BAD_REQUEST)