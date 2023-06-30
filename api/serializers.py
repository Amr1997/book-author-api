from rest_framework import serializers
from .models import Author, Book, Page, CustomUser

class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'is_author')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        is_author = validated_data.pop('is_author', False)
        user = CustomUser.objects.create_user(**validated_data)
        if is_author:
            Author.objects.create(user=user)
        return user

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'
