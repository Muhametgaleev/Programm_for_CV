from django.db import models, OperationalError


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField(verbose_name="Название")
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(verbose_name="Число копий", default=1, editable=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена", default=1.00)
