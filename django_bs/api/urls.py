from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter

from api.views import *


#router = DefaultRouter()
#router.register(r'books', BookViewSet)
#router.register(r'authors', AuthorViewSet)

#urlpatterns = [
#    url(r'^', include(router.urls))
#]

author_urls = [
    url(r'^/$', AuthorViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^/(?P<pk>[0-9]+)$', AuthorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

book_urls = [
    url(r'^/$', BookViewSet.as_view({'get': 'list'})),
    url(r'^/(?P<pk>[0-9]+)$', BookViewSet.as_view({'get': 'list'})),
]

authorbook_urls = [
    url(r'^/$', AuthorBookViewSet.as_view({'get': 'list'})),
]

college_urls = [
    url(r'^/$', CollegeViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^/(?P<pk>[0-9]+)$', CollegeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

course_urls = [
    url(r'^/$', CourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^/(?P<pk>[0-9]+)$', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

coursebook_urls = [
    url(r'^/$', CourseBookViewSet.as_view({'get': 'list'})),
]

listing_urls = [
    url(r'^/$', ListingViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^/(?P<pk>[0-9]+)$', ListingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

user_urls = [
    url(r'^/$', UserViewSet.as_view({'post': 'authenticate'})),
    url(r'^/(?P<pk>[0-9]+)$', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

userinfo_urls = [
    url(r'^/$', UserInfoViewSet.as_view({'post': 'create'})),
    url(r'^/(?P<pk>[0-9]+)$', UserInfoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

urlpatterns = [
    url(r'^authors', include(author_urls)),
    url(r'^books', include(book_urls)),
    url(r'^authorbooks', include(authorbook_urls)),
    url(r'^colleges', include(college_urls)),
    url(r'^courses', include(course_urls)),
    url(r'^coursebooks', include(coursebook_urls)),
    url(r'^listings', include(listing_urls)),
    url(r'^users', include(user_urls)),
    url(r'^userinfo', include(userinfo_urls)),
]
