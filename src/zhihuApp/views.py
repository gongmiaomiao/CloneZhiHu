from django.shortcuts import render
from zhihuApp.models import User
from django.http import  HttpResponse
from django.shortcuts import redirect
# Create your views here.

# def home(request):
# 	return render(request, 'home.html')

def signin(request):
	if request.method == 'POST':
		input_phone = request.POST['account']
		input_password = request.POST['password']
		user = User.objects.filter(
			phone = input_phone,
			password =  input_password,
			)[0]
		
		if user == None:
			return HttpResponse("mistake input")
		else:
			return redirect('http://www.clonezhihu.com:8000/people/'+str(user.id))
	else:
		return render(request, 'home.html')
	
def people(request,user_id):
	user = User.objects.get(id = user_id)
	ctx = {'user':user, 'user_question':user.question_set.all()}
	if  request.method == "GET":
		return render(request,'people.html',ctx)
	
def asks(request,user_id):
	user = User.objects.get(id = user_id)
	ctx = {'user':user, 'user_question':user.question_set.all()}
	if  request.method == "GET":
		return render(request,'asks.html',ctx)