from django.contrib import admin

from app import models


class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    list_display = ("question_text", "pub_date",)
    inlines = [ChoiceInline]


# Register your models here.
admin.site.register(models.District)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)

