from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from django.contrib import messages
from rest_framework.exceptions import ValidationError

from .models import Article

from .forms import Register_form, Arti_form


# Create your views here.
def home(request):
    heading = Article.objects.only('title','image','date').order_by('-date')

    paginator = Paginator(heading, 5)

    page_number = request.GET.get('page')

    pageobj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page': pageobj})

def register(request):
    form = Register_form()
    if request.method=='POST':
        form = Register_form(request.POST)


        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("home")

    return render(request,'register.html',{'form':form})

@login_required()
def publish (request):
    aform = Arti_form()
    if request.method=='POST':
        aform= Arti_form(request.POST,request.FILES)


        if aform.is_valid():


           article = aform.save(commit=False)
           article.author=request.user
           article.save()
           return redirect("home")
    return render(request,'publish.html',{'a':aform})

def content(request,con_id):
    con = get_object_or_404(Article,id=con_id)

    return render(request,'content.html',{'c':con})


@login_required()
def profile (request):
    article = request.user
    user_article = Article.objects.filter(author=article)

    return render(request,'profile.html',{'article':user_article} )

@login_required()
def update(request,con_id):

    update_arti = get_object_or_404(Article,id=con_id,author=request.user)

    if request.method == 'POST':
        form = Arti_form(request.POST, request.FILES, instance=update_arti)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            raise ValidationError('unsuccessful update')
    else:
        form = Arti_form(request.POST, request.FILES, instance=update_arti)
        return render(request,'update.html',{'form':form})
@login_required()
def delete(request):
    if request.method=='POST':
      delete_arti = int(request.POST.get('arti_id'))


      del_arti = get_object_or_404(Article,id=delete_arti,author=request.user).delete()

    return redirect('profile')