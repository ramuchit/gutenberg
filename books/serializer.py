from rest_framework import serializers
from .models import Book, Subject, Author, Language, Bookshelf, Format


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'birth_year', 'death_year')


class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ('name',)


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ('url', 'mime_type')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('code',)


class OutputSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    authors = AuthorSerializer(many=True, read_only=True)
    bookshelves = BookshelfSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    formats = FormatSerializer(many=True)

    class Meta:
        model = Book
        fields = ('title', 'subjects', 'authors', 'languages', 'bookshelves', 'formats')
