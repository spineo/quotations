from django.contrib import admin

from myquotes.models import Author, Quotation, Event, Keyword, QuotationLastShown, QuotationKeyword, EventAuthor, EventKeyword

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'description' ]
    ordering     = ['full_name']

admin.site.register(Author, AuthorAdmin)

admin.site.register(Quotation)

class EventAdmin(admin.ModelAdmin):
    ordering     = ['event']

admin.site.register(Event, EventAdmin)

admin.site.register(Keyword)
admin.site.register(QuotationLastShown)
admin.site.register(QuotationKeyword)
admin.site.register(EventAuthor)
admin.site.register(EventKeyword)
