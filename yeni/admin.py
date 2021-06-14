# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Question, Choice
#StackedInline 대신에 TabularInline을 사용하면, 
# 관련된 객체는 좀 더 조밀하고 테이블 기반 형식으로 표시
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
   
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']
admin.site.register(Question, QuestionAdmin)
