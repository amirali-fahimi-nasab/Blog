
from rest_framework import serializers

from django.contrib.auth.models import User


class UserRegisterSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=200 , required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=100 , required=True ,write_only=True)
    # password2 = serializers.CharField(max_length=100 , required=True ,write_only=True)

    def validate_username(self,value):
        if value == 'admin':
            raise  serializers.ValidationError('The username must be admin')

        return value


    def validate(self,view):
        if view['password'] != view['password2']:
            raise serializers.ValidationError('The password not match')

        return view




class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
