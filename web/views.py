from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Document
from .forms import DocumentForm
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def main(request):
    return render(request, 'main.html', {})
def index(request):
    return render(request, 'index.html', {})
def base(request):
    return render(request, 'base.html', {})

@login_required
def account(request):
    return render(request, 'account.html', {})

def library(request):
    return render(request, 'library.html', {})
def bgm(request):
    return render(request, 'bgm.html', {})
def photo(request):
    return render(request, 'photo.html', {})
def hot(request):
    return render(request, 'hot.html', {})

def community(request):
    blogs = Post.objects
    return render(request, 'community.html', {'blogs' : blogs})
def new(request):
    return render(request, 'new.html', {})
def create(request):
    blog = Post()
    blog.title = request.GET['title']
    blog.text = request.GET['text']
    blog.created_date = timezone.datetime.now()
    blog.save()
    return

#def detail(request, blog_id):
   # blog_detail = get_object_or_404(Post, pk=blog_id)
    #return render(request, 'detail.html', {'community': blog_detail})

def upload(request):
    return render(request, 'upload.html', {})

def customer(request):
    return render(request, 'customer.html', {})
def team(request):
    return render(request, 'team.html', {})
def bgm2(request):
    return render(request, 'bgm2.html', {})
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            auth.login(request, user)
            return redirect('hyunsoo')
        messages.error(request, '비밀번호가 일치하지 않습니다')
        return render(request, 'signup.html')

    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('hyunsoo')
        else:
            messages.error(request, '잘못된 아이디 혹은 비밀번호를 입력하셨습니다')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('hyunsoo')

def photo_animal(request):
    return render(request, 'photo_animal.html', {})
def photo_building(request):
    return render(request, 'photo_building.html', {})
def photo_emotion(request):
    return render(request, 'photo_emotion.html', {})
def photo_food(request):
    return render(request, 'photo_food.html', {})
def photo_music(request):
    return render(request, 'photo_music.html', {})
def photo_nature(request):
    return render(request, 'photo_nature.html', {})
def photo_people(request):
    return render(request, 'photo_people.html', {})
def photo_sport(request):
    return render(request, 'photo_sport.html', {})

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            return HttpResponseRedirect(reverse('upload_file'))
    else:
        form = DocumentForm()

    documents = Document.objects.all()

    return render(request, 'upload.html', {'documents':documents, 'form':form})
def delete_matrix():
    documents = Document.objects.all()
    for document in documents:
        document.delete()