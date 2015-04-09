from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'author'


class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=100)
    edition = models.IntegerField()

    def __unicode__(self):
        return u'%s %s %d' % (self.isbn, self.title, self.edition)

    class Meta:
        managed = False
        db_table = 'book'


class AuthorBook(models.Model):
    author = models.ForeignKey(Author)
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return u'%s %s' % (self.author.name, self.book.title)

    class Meta:
        managed = False
        db_table = 'author_book'
        unique_together = ['author', 'book']

class College(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'college'


class Course(models.Model):
    college = models.ForeignKey(College)
    title = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=4)
    number = models.CharField(max_length=6)

    def __unicode__(self):
        return u'%s, %s%s - %s' % (self.college.name, self.abbreviation, self.number, self.title)

    class Meta:
        managed = False
        db_table = 'course'


class CourseBook(models.Model):
    course = models.ForeignKey(Course)
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return u'%s %s' % (self.course.title, self.book.title)

    class Meta:
        managed = False
        db_table = 'course_book'
        unique_together = ['course', 'book']


class Listing(models.Model):
    user = models.ForeignKey('User')
    book = models.ForeignKey(Book)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    book_condition = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s %f' % (self.user.username, self.book.title, self.price)

    class Meta:
        managed = False
        db_table = 'listing'


class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=44)
    salt = models.CharField(max_length=16)
    role = models.CharField(max_length=20)
    created = models.DateTimeField()
    last_login = models.DateTimeField()

    def __unicode__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'user'


class UserInfo(models.Model):
    user = models.ForeignKey(User)
    college = models.ForeignKey(College)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        managed = False
        db_table = 'user_info'
