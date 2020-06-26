from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import calendar
from datetime import date

# The primary key field for each class is auto-generated
#
class Author(models.Model):
    full_name        = models.CharField(max_length=100, unique=True)
    birth_date       = models.DateField(null=True)
    death_date       = models.DateField(null=True)
    description      = models.CharField(max_length=200, null=True)
    bio_extract      = models.CharField(max_length=800, null=True)
    bio_source_url   = models.URLField(null=True)

class Quotation(models.Model):
    quotation        = models.CharField(max_length=200, unique=True)
    source           = models.CharField(max_length=100, null=True)
    author           = models.ForeignKey(Author, on_delete=models.CASCADE)

class Event(models.Model):
    MONTH_CHOICES    = [(str(i), calendar.month_name[i]) for i in range(1,13)]
    SEASON_CHOICES   = [
        ('Winter', 'Winter'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall',   'Fall'),
    ]

    def max_value_current_year():
        return date.today().year

    event            = models.CharField(max_length=400, unique=True)
    day              = models.IntegerField(validators=[MaxValueValidator(31), MinValueValidator(1)], null=True) 
    month            = models.CharField(max_length=9, choices=MONTH_CHOICES, default=1, null=True)
    year             = models.IntegerField(validators=[MaxValueValidator(max_value_current_year()+1), MinValueValidator(-1000)], null=True)
    season           = models.CharField(max_length=6, choices=SEASON_CHOICES, null=True)

    def __str__(self):
        return self.event

class Keyword(models.Model):
    keyword          = models.CharField(max_length=50, unique=True)

class QuotationLastShown(models.Model):
    quotation        = models.OneToOneField(Quotation, on_delete=models.CASCADE)
    last_shown_date  = models.DateField()

class QuotationKeyword(models.Model):
    quotation        = models.OneToOneField(Quotation, on_delete=models.CASCADE)
    keyword          = models.ManyToManyField(Keyword)

class EventAuthor(models.Model):
    event            = models.OneToOneField(Event, on_delete=models.CASCADE)
    author           = models.OneToOneField(Author, on_delete=models.CASCADE)

class EventKeyword(models.Model):
    event            = models.ManyToManyField(Event)
    keyword          = models.ManyToManyField(Keyword)
