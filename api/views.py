from django.db.models import Prefetch
from rest_framework import viewsets
from .models import Author, Book, Page
from .serializers import AuthorSerializer, BookSerializer, PageSerializer
from .permissions import IsAuthorOrReadOnly

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthorOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().prefetch_related(Prefetch('pages', queryset=Page.objects.all()))
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly]

class PageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        queryset = Page.objects.filter(book_id=book_id)
        return queryset
