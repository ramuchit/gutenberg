from rest_framework import generics
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from functools import reduce
import operator
from .models import Book
from .serializer import OutputSerializer


class BookListView(generics.ListAPIView):
    serializer_class = OutputSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get_queryset(self):
        queryset = Book.objects.all().order_by('-download_count')
        # search by language
        language = self.request.query_params.get('language')
        if language is not None:
            queryset = queryset.filter(languages__code__in=language.split(','))

        # search by subject or bookshelf name
        topic = self.request.query_params.get('topic')
        if topic is not None:
            search_set = reduce(operator.or_, (Q(subjects__name__icontains=x) | Q(bookshelves__name__icontains=x)
                                               for x in topic.split(',')))
            queryset = queryset.filter(search_set).distinct()

        # search by author
        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(authors__name__icontains=author)

        # search by title
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        # search by Mime Type
        mime_type = self.request.query_params.get('mime-type')
        if mime_type is not None:
            queryset = queryset.filter(formats__mime_type__icontains=mime_type)

        return queryset

