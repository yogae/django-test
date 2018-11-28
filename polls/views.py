from django.http import HttpResponseRedirect, HttpResponse

# from django.core.urlresolvers import reverse
# 변경되었음
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from polls.models import Choice, Question
from django.views import generic
import logging

logger = logging.getLogger(__name__)

# 클래스 뷰로 변경
# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     return render(request, 'polls/index.html', {'latest_qustion_list': latest_question_list})


# ListView를 상속받는 경우는 객체가 들어있는 리스트를 구성해서 이를 컨텍스트 변수로 템플릿 시스템에 넘겨주면 됩니다.
# 만일 이런 리스트를 테이블에 들어있는 모든 레코드를 가져와 구성하는 경우에는 테이블명, 즉 모델 클래스명만 지정해주면 됩니다.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lastest_question_list'
    def get_queryset(self):
        # 최근 생성된 질문 5개를 반환함
        return Question.objects.order_by('-pub_date')[:5]
    
# 클래스 뷰로 변경
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# DetailView를 상속받는 경우는 특정 객체 하나를 컨텍스트 변수에 담아서 템플릿 시스템에 넘겨주면 됩니다.
# 만일 특정 객체를 데이블에서 Primary Key로 조회해서 가져오는 경우에는 테이블명, 즉 모델 클래스명만 지정해주면 됩니다.
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

def vote(request, question_id):
    # __name__은 모듈 경로를 담고 있는 파이썬 내장 변수
    # polls.views
    logger.debug("vote().question_id: %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_mesage': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# 클래스 뷰로 변경
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'