from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter , NestedDefaultRouter
from .views import AuthorViewSet, BookViewSet, PageViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

books_router = NestedDefaultRouter(router, r'books', lookup='book')
books_router.register(r'pages', PageViewSet, basename='book-pages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(books_router.urls)),
]