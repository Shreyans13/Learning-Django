from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Question

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index. ")
    # return HttpResponse(', '.join([q.question_text for q in Question.objects.order_by('-pub_date')[:5]]))
    # return HttpResponse(loader.get_template('polls/index.html').render({'latest_question_list': Question.objects.order_by('-pub_date')[:5]}, request))
    # using shortcut
    return render(request, 'polls/index.html', {'latest_question_list': Question.objects.order_by('-pub_date')[:5]})

def detail(request, question_id):
    # return HttpResponse("You`re looking at question %s. " % question_id)
    # try:
    #     return render(request, 'polls/detail.html', {'question' : Question.objects.get(pk=question_id)})
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # using shortcut
    return render(request, 'polls/detail.html', {'question': get_object_or_404(Question, pk=question_id)})

def results(request, question_id):
    response = "You`re looking at the results of question %s. "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s. " % question_id)