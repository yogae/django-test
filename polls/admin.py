from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    # Choice 모델 클래스 같이 보기
    inlines = [ChoiceInline] 
    # 레코드 리스트 걸럼 항목 지정
    # model.py에서 정의한 __str()__ 메소드의 리텀값을 레코드의 제목으로 사용
    list_display = ('question_text', 'pub_date') 
    # 필터 사이드바 추가
    list_filter = ['pub_date']
    # 검색 박스 추가
    search_fields = ['question_test'] 

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes') 
    


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)