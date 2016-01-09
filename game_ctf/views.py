#
# @author:metastableB
# views.py
# 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.urlresolvers import resolve, Resolver404, is_valid_path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from models import Question
from .settings import QUESTIONS_DIR, info_messages, template_path

@login_required 
def home(request):
	questions = Question.objects.all().filter(valid=True)
	return render(request, 'game_ctf/home.html',{'questions':questions})


@login_required
def question_page(request,question_id):
	try:
		question = Question.objects.get(pk = question_id)
	except ObjectDoesNotExist:
		messages.add_message(request,
			info_messages['question does not exist'][0],info_messages['question does not exist'][1])
		return HttpResponseRedirect(reverse('game_ctf:home'))
	
	# TODO : Check if the user/team has already answered the question
	return render(request, QUESTIONS_DIR + question.source_file)

@login_required 
def leaderboard(request):
	return HttpResponse("Apparently you are winning")