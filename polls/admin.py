from django.contrib import admin
from .models import Question,Choice

class ChoiceInLine(admin.TabularInline):

    #alt-StackedInLine
	
    model = Choice
    extra = 3 #default no. of choices
	
class QuestionAdmin(admin.ModelAdmin):

    fieldsets=[
      (None , {'fields':['question_text'] }),
      ('Date Information' , {'fields':['pub_date'] , 'classes':['collapse'] }),
    ]
	
    list_display = ('question_text','pub_date','recently_published')
    list_filter = ['pub_date']

    search_fields = ['question_text']
    
    inlines=[ChoiceInLine]

admin.site.register(Question,QuestionAdmin)

