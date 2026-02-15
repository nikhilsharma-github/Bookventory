from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    # Way 1 
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context,request))
    # Way 2
    return render(request,"polls/index.html",context)

def detail(request, question_id):
    # Way 1 
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist")
    # Way 2
    question = get_object_or_404(Question, pk=question_id)
    return render(request,"polls/details.html",{"question":question})


def results(request, question_id):
    response = "You are looking at the result of the Question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting for the Question %s",question_id)