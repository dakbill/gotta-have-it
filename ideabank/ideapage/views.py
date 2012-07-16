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
			print str(uname)
			user=authenticate(username=uname,password=passw)
			if user is not None:
				if user.is_active:
					print 'Correct username and password'
					return HttpResponseRedirect('ideapage/login.html')
				else:
					print 'Account disabled'
			else:
				print 'Incorrect password'   
		elif ((request.POST.keys()[0])=='comments'):
			newcomment=request.POST.get('newcom') 
			print newcomment
			p=Comment(idea=todays_idea ,body='CRAZY', author='i will have to get it' ,updated=datetime.now()) 
			p.save()
		elif not ((request.POST.keys()[0])=='username') and not ((request.POST.keys()[0])=='comments'):
			pass    
	t = loader.get_template('ideapage/base.html')
	c = Context({'todays_idea':todays_idea,'comments':comments })
	return HttpResponse(t.render(c))
class CommentForm(ModelForm):
	class Meta:
		model=Comment
		exclude=['idea']
