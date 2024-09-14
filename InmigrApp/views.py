from django.shortcuts import render
from .forms import CreatedUserForm

def index(request):

    return render(request= request, template_name= 'index.html')

def about(request):
    
    return render(request= request, template_name= 'about.html')

def login(request):

    return render(request= request, template_name= 'login.html')

def register(request):

    form = CreatedUserForm()

    if request.method == 'POST':

        form= CreatedUserForm(request.POST)
        
        if form.is_valid():

            form.save()

    context= {'form': form}

    return render(request= request, template_name= 'register.html',  context= context)