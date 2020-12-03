from django.contrib import admin
from .models import Choice, Question

# Register your models here.
# class ChoiceInLine(admin.StackedInline):
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    # fields=['pub_date', 'question_text']
    # fields=['question_text','pub_date']
    # fieldsets = [
    #     (None, {'fields': ['question_text']}),
    #     ('Date Information', {'fields' : ['pub_date']})
    # ]
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields' : ['pub_date'], 'classes' : ['collapse']})
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)