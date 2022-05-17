from django.urls import path, include
from books.views import BookListView

urlpatterns = [
    path("books", BookListView.as_view()),
]
