
from rest_framework import serializers
from .models import Blog,Comment

class BlogSerializers(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = "__all__"
        extra_kwargs = {'choices_wishlist':{'required':False}}

    def get_comments(self,obj):
        result = obj.comments.all()
        return CommentSerializers(instance=result, many=True).data



class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ="__all__"


