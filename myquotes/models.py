from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import calendar

# The primary key field for each class is auto-generated
#
class Author(models.Model):
    full_name        = models.CharField(max_length=100, unique=True)
    birth_date       = models.DateField()
    death_date       = models.DateField()
    bio_extract      = models.CharField(max_length=400)
    bio_source_url   = models.URLField()

class Quotation(models.Model):
    quotation        = models.CharField(max_length=200, unique=True)
    quotation_source = models.CharField(max_length=100, null=True)
    author_id        = models.ForeignKey(Author, on_delete=models.CASCADE)

class Event(models.Model):
    MONTH_CHOICES    = [(str(i), calendar.month_name[i]) for i in range(1,13)]
    SEASON_CHOICES   = [
        ('WINTER', 'Winter'),
        ('SPRING', 'Spring'),
        ('SUMMER', 'Summer'),
        ('FALL',   'Fall'),
    ]

    def current_year():
        return datetime.date.today().year

    def max_value_current_year(value):
        return MaxValueValidator(current_year())(value)

    event            = models.CharField(max_length=100, unique=True)
    day              = models.IntegerField(validators=[MaxValueValidator(31), MinValueValidator(1)], null=True) 
    month            = models.CharField(max_length=9, choices=MONTH_CHOICES, default=1, null=True)
    year             = models.IntegerField(validators=[max_value_current_year, MinValueValidator(-1000)], null=True)
    season           = models.CharField(max_length=6, choices=SEASON_CHOICES, null=True)

class Keyword(models.Model):
    keyword          = models.CharField(max_length=50, unique=True)

class QuotationLastShown(models.Model):
    quotation_id     = models.OneToOneField(Quotation, on_delete=models.CASCADE)
    last_shown_date  = models.DateField()

class QuotationKeyword(models.Model):
    quotation_id     = models.OneToOneField(Quotation, on_delete=models.CASCADE)
    keyword_id       = models.ManyToManyField(Keyword)

class EventAuthor(models.Model):
    event_id         = models.OneToOneField(Event, on_delete=models.CASCADE)
    author_id        = models.OneToOneField(Author, on_delete=models.CASCADE)

class EventKeyword(models.Model):
    event_id         = models.ManyToManyField(Event)
    keyword_id       = models.ManyToManyField(Keyword)
