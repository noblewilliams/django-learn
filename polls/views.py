from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

def index (request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {
    'latest_question_list': latest_question_list,
  }
  return render(request, 'polls/index.html', context)

def detail (request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})
  

def results (request, question_id):
  result_response = "You're looking at the results of the question %s."
  return HttpResponse(result_response % question_id) 

def vote (request, question_id):
  vote_response = "You're voting on Question %s."
  return HttpResponse(vote_response % question_id)