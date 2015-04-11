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
        queryset = AuthorBook.objects.raw('SELECT book.id, book.isbn, book.title, book.edition FROM author_book JOIN book ON book.id = author_book.book_id WHERE author_book.author_id = ' + str(obj.id) + ';')
        serializer = BookWithoutAuthorsSerializer(queryset, many=True)
        return serializer.data


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()

    class Meta:
        model = Book

    def get_authors(self, obj):
        queryset = AuthorBook.objects.raw('SELECT author.id, author.name FROM author_book JOIN author ON author.id = author_book.author_id WHERE author_book.book_id = ' + str(obj.id) + ';')
        serializer = AuthorWithoutBooksSerializer(queryset, many=True)
        return serializer.data


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
        queryset = CourseBook.objects.raw('SELECT book.id, book.isbn, book.title, book.edition FROM course_book JOIN book ON book.id = course_book.book_id WHERE course_book.course_id = ' + str(obj.id) + ';')
        seiralizer = BookSerializer(queryset, many=True)
        return serializer.data


class CourseBookSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False, read_only=True)
    book = BookSerializer(many=False, read_only=True)

    class Meta:
        model = CourseBook
        fields = ['course', 'book']


class UserSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('password', 'salt')

    def get_user_info(self, obj):
        queryset = User.objects.raw('SELECT user_info.id, user_info.college_id, user_info.first_name, user_info.last_name, user_info.email, user_info.address, user_info.phone_number FROM user_info JOIN user ON user.id = user_info.user_id WHERE user_info.user_id = ' + str(obj.id) + ';')
        serializer = UserInfoSerializer(queryset[0])
        return serializer.data


class ListingSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    book = BookSerializer(many=False, read_only=True)

    class Meta:
        model = Listing


class UserWithoutInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'salt')

class UserInfoSerializer(serializers.ModelSerializer):
    user = UserWithoutInfoSerializer(many=False, read_only=True)
    college = CollegeSerializer(many=False, read_only=True)

    class Meta:
        model = UserInfo
