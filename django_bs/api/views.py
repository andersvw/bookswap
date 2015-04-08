from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from api.models import *
from api.serializers import *

import hashlib, random, json

#Randomly chosen alphabet that includes most of the ASCII character set (without some used in SQL syntax)
alphabet = " !#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorBookViewSet(viewsets.ModelViewSet):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBookSerializer

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseBookViewSet(viewsets.ModelViewSet):
    queryset = CourseBook.objects.all()
    serializer_class = CourseBookSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def authenticate(self, request):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        try:
            user = User.objects.get(username=username)
        except DoesNotExist:
            content = {'username' : username, 'issue': 'Username not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        saltedpass = password + str(user.salt)
        hashedpass = hashlib.sha512(saltedpass).hexdigest()

        if(str(user.password) == hashedpass):
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            content = {'username': username, 'issue': 'Incorrect password'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def signup(self, request):
        #salt = ''.join(random.SystemRandom().choice(alphabet) for _ in xrange(16)))
        pass


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
