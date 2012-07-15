from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Idea, Comment 
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django import forms
@csrf_exempt
def home(request):
	todays_idea=Idea.objects.get(pk=1)
	comments=Comment.objects.filter(idea=todays_idea)
	t = loader.get_template('ideapage/base.html')
	c = Context({'todays_idea':todays_idea,'comments':comments })
		
    	return HttpResponse(t.render(c))

