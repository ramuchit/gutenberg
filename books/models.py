from django.db import models

# Create your models here.


class Author(models.Model):
	name = models.CharField(max_length=128)
	birth_year = models.SmallIntegerField(null=True)
	death_year = models.SmallIntegerField(null=True)


class Bookshelf(models.Model):
	name = models.CharField(max_length=64)


class Subject(models.Model):
	name = models.TextField()


class Language(models.Model):
	code = models.CharField(max_length=4)


class Book(models.Model):
	title = models.TextField()
	download_count = models.IntegerField(null=True)
	gutenberg_id = models.IntegerField()
	media_type = models.CharField(max_length=16)
	authors = models.ManyToManyField(Author, related_name="book_author")
	subjects = models.ManyToManyField(Subject, related_name="book_subject")
	bookshelves = models.ManyToManyField(Bookshelf, related_name="book_shelf")
	languages = models.ManyToManyField(Language, related_name="book_lang")


class Format(models.Model):
	mime_type = models.CharField(max_length=32)
	url = models.TextField()
	book = models.ForeignKey(Book, related_name='formats', on_delete=models.CASCADE)
