from rest_framework import serializers
from api.models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book


class AuthorBookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)
    book = BookSerializer(many=False, read_only=True)

    class Meta:
        model = AuthorBook
        fields = ['author', 'book']

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course


class CourseBookSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False, read_only=True)
    book = BookSerializer(many=False, read_only=True)

    class Meta:
        model = CourseBook
        fields = ['course', 'book']


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo


