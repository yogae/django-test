from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    # N:N
    authors = models.ManyToManyField('Author') 
    # N:1
    # ForeignKey를 사용시 on_delete option은 필수
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE) 
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100)
    email = models.EmailField()
    

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name
