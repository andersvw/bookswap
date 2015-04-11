from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from api.models import *
from api.serializers import *

import hashlib, random, json, datetime, warnings, exceptions

warnings.filterwarnings('ignore', category=exceptions.RuntimeWarning, message='DateTimeField User.last_login received a naive datetime')
warnings.filterwarnings('ignore', category=exceptions.RuntimeWarning, message='DateTimeField User.created received a naive datetime')

#Randomly chosen alphabet that includes most of the ASCII character set (without some used in SQL syntax)
alphabet = " !#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request):
        name = request.QUERY_PARAMS.get('name', None)

        queryset = Author.objects.all()
        if name is not None:
            # icontains is a case-insensitive containment test
            queryset = queryset.filter(name__icontains=name)

        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        isbn = request.QUERY_PARAMS.get('isbn', None)
        title = request.QUERY_PARAMS.get('title', None)
        edition = request.QUERY_PARAMS.get('edition', None)

        queryset = Book.objects.all()
        if isbn is not None:
            queryset = queryset.filter(isbn__icontains=isbn)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if edition is not None:
            queryset = queryset.filter(edition=edition)

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


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
        username = request.QUERY_PARAMS.get('username', None)
        password = request.QUERY_PARAMS.get('password', None)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            content = {'username' : username, 'issue': 'Username not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        saltedpass = str(password) + str(user.salt)
        hashedpass = hashlib.sha512(saltedpass).hexdigest()

        if(str(user.password) == hashedpass):
            user.last_login = datetime.datetime.now()
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            content = {'username': username, 'issue': 'Incorrect password'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def signup(self, request):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        try:
            user = User.objects.get(username=username)
            content = {'username' : username, 'issue': 'Username already taken'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            pass

        # Generates a random 16 character long salt value
        # The available character set (alphabet) is at the top of the file
        salt = ''.join(random.SystemRandom().choice(alphabet) for _ in xrange(16))
        saltedpass = str(password) + salt
        hashedpass = hashlib.sha512(saltedpass).hexdigest()

        user = User(username=str(username), password=password, salt=salt, created=datetime.datetime.now(), last_login=datetime.datetime.now())
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)



class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
