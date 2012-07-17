from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Idea, Comment 
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

@csrf_exempt
def home(request):
	todays_idea=Idea.objects.get(pk=1)
	comments=Comment.objects.filter(idea=todays_idea)
	if request.method == 'POST':
		if ((request.POST.keys()[0])=='username'):
			uname=request.POST.get('username')
			passw=request.POST.get('password')
			user=authenticate(username=uname,password=passw)
			if user is not None:
				if user.is_active:
					request.session['username']=uname
					print 'Correct username and password'
					return HttpResponseRedirect('logged_in')
				else:
					print 'Account disabled'
			else:
				print 'Incorrect password'   
		
		elif not ((request.POST.keys()[0])=='username') and not ((request.POST.keys()[0])=='comments'):
			pass    
	t = loader.get_template('ideapage/base.html')
	c = Context({'todays_idea':todays_idea,'comments':comments })
	return HttpResponse(t.render(c))
@csrf_exempt
def logged_in(request):
	username=request.session['username']
	todays_idea=Idea.objects.get(pk=1)
	if request.method == 'POST':
		if ((request.POST.keys()[0])=='newcom'):
			newcomment=request.POST.get('newcom') 
			p=Comment(idea=todays_idea ,body=newcomment, author=username ,updated=datetime.now()) 
			p.save()
		elif not ((request.POST.keys()[0])=='username') and not ((request.POST.keys()[0])=='comments'):
			pass
	comments=Comment.objects.filter(idea=todays_idea)
	t = loader.get_template('ideapage/logged_in.html')
	c = Context({'todays_idea':todays_idea,'comments':comments,'username':username })
	return HttpResponse(t.render(c))
@csrf_exempt
def out(request):
	     #logout(request)
	     request.path='/ideapage'
	     response = HttpResponseRedirect(request.path)
	     response.delete_cookie('user_location')
	     return response
