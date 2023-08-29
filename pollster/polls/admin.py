from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# Change the site header and title
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin Area"

# Making choices related to questions
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]

# Register poll models
# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)