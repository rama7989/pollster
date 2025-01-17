from django.contrib import admin
from .models import Question,Choice


# # Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_text','pub_date')
    search_fields=('question_text',)

class ChoiceAdmin(admin.ModelAdmin):
    list_display=('choice_text','votes','question')


# Customizing the admin site interface
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin Area"


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)


# from django.contrib import admin

# from .models import Question, Choice

# admin.site.site_header = "Pollster Admin"
# admin.site.site_title = "Pollster Admin Area"
# admin.site.index_title = "Welcome to the Pollster Admin Area"


# class ChoiceInLine(admin.TabularInline):
#     model = Choice
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
#         'fields': ['pub_date'], 'classes': ['collapse']}), ]
#     inlines = [ChoiceInLine]


# admin.site.register(Question, QuestionAdmin)

