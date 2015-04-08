from rest_framework import serializers
from api.models import *



class AuthorWithoutBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class BookWithoutAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author

    def get_books(self, obj):
        booksqueryset = AuthorBook.objects.raw('SELECT book.id, book.isbn, book.title, book.edition FROM author_book JOIN book ON book.id = author_book.book_id WHERE author_book.author_id = ' + str(obj.id) + ';')
        books = []
        for book in booksqueryset:
            serializer = BookWithoutAuthorsSerializer(book)
            books.append(serializer.data)
        return books


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()

    class Meta:
        model = Book

    def get_authors(self, obj):
        authorsqueryset = AuthorBook.objects.raw('SELECT author.id, author.name FROM author_book JOIN author ON author.id = author_book.author_id WHERE author_book.book_id = ' + str(obj.id) + ';')
        authors = []
        for author in authorsqueryset:
            serializer = AuthorWithoutBooksSerializer(author)
            authors.append(serializer.data)
        return authors


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
    college = CollegeSerializer(many=False, read_only=True)
    required_books = serializers.SerializerMethodField()

    class Meta:
        model = Course

    def get_required_books(self, obj):
        booksqueryset = CourseBook.objects.raw('SELECT book.id, book.isbn, book.title, book.edition FROM course_book JOIN book ON book.id = course_book.book_id WHERE course_book.course_id = ' + str(obj.id) + ';')
        books = []
        for book in booksqueryset:
            serializer = BookSerializer(book)
            books.append(serializer.data)
        return books


class CourseBookSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False, read_only=True)
    book = BookSerializer(many=False, read_only=True)

    class Meta:
        model = CourseBook
        fields = ['course', 'book']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('username', 'password')
        exclude = ('id', 'salt')


class ListingSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    book = BookSerializer(many=False, read_only=True)

    class Meta:
        model = Listing


class UserInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    college = CollegeSerializer(many=False, read_only=True)

    class Meta:
        model = UserInfo
