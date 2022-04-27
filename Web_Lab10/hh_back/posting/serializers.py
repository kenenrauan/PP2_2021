from rest_framework import serializers

from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    # company = CompanySerializer2()
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'like_cnt', 'created_at', 'category' )
        # read_only_fields = ('name',)