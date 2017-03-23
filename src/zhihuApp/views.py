from django.shortcuts import render
from zhihuApp.models import User, Question, Answers, Collections
from django.http import  HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
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
# 			return redirect('http://www.clonezhihu.com:8000/people/'+str(user.id))
			return redirect('http://127.0.0.1:8000/people/'+str(user.id))
	else:
		return render(request, 'home.html')
	
def people(request,user_id):
	user = User.objects.get(id = user_id)
	ctx = {'user':user, 'user_question':user.question_set.all()}
	if  request.method == "POST":
		input_title = request.POST['title']
		input_content = request.POST['content']
		
		add = Question()
		add.user = user
		add.title = input_title
		add.content =  input_content
		add.release_date = timezone.now()
		add.save()
		
		ctx = {'user':user, 'user_question':user.question_set.all()}
		return render(request,'people.html',ctx)
	else:
		return render(request,'people.html',ctx)
	
def asks(request,user_id):
	user = User.objects.get(id = user_id)
	ctx = {'user':user, 'user_question':user.question_set.all()}
	if  request.method == "POST":
		input_title = request.POST['title']
		input_content = request.POST['content']
		
		add = Question()
		add.user = user
		add.title = input_title
		add.content =  input_content
		add.release_date = timezone.now()
		add.save()
		
		ctx = {'user':user, 'user_question':user.question_set.all()}
		return render(request,'asks.html',ctx)
	else:
		return render(request,'asks.html',ctx)

def asksdetail(request,user_id, question_id):
	user = User.objects.get(id = user_id)
	question = Question.objects.get(id = question_id)
	
	if  request.method == 'POST':
		input_answer = request.POST['add']
		addans = Answers()
		addans.user = user
		addans.question = question
		addans.content = input_answer
		addans.release_date = timezone.now()
		addans.save()
			
	ctx = {'user':user,'question':question,'answers':question.answers_set.all()}
	return  render(request,'asksdetail.html',ctx)


def answers(request,user_id):
	user = User.objects.get(id = user_id)
	ctx = {'user':user, 'user_answers':user.answers_set.all()}	
	if  request.method == "POST":
		input_title = request.POST['title']
		input_content = request.POST['content']
		
		add = Question()
		add.user = user
		add.title = input_title
		add.content =  input_content
		add.release_date = timezone.now()
		add.save()
		
		ctx = {'user':user, 'user_answers':user.answers_set.all()}
		return render(request,'answers.html',ctx)
	else:
		return render(request,'answers.html',ctx)

def collections(request,user_id):
	user = User.objects.get(id = user_id)
	collections =  Collections.objects.all()
	
	distinct = list()
	for i in collections:
		if i.collectionname  not in distinct:
			distinct.append(i.collectionname)	
	
	last_update = list()
	for i in distinct:
		uplist = Collections.objects.filter(collectionname = i).last()
		last_update.append(uplist.release_date)
	
	newarr = zip(distinct, last_update)		
	
	ctx = {'user':user, 'distinct':newarr}
	if request.method == "GET":
		return render(request,'collections.html',ctx)
	
	
	
	