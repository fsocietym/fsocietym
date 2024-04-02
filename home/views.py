from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(response):
    emp = [
        {'Name': 'Noor', 'Age': 18, 'Salary': 6000},
        {'Name': 'Rahul', 'Age': 20, 'Salary': 3500},
        {'Name': 'Saud', 'Age': 19, 'Salary': 4500},
        {'Name': 'Saurabh', 'Age': 19, 'Salary': 4500}
    ]

    return render(response, 'index.html', context={'peoples': emp})


def about(response):
    page_title = 'About Us'
    return render(response, 'about.html', context={'PageTitle':page_title})


def contact(response):
    page_title = 'Contact Us'
    user_data = ''
    if response.POST:
        user_data = response.POST.get('email')
        print(user_data)
    
    return render(response, 'contact.html', context={'PageTitle':page_title, 'mail':user_data}) 
    
def recipes(response):
    page_title = 'Recipes'
    if response.method == 'POST':
        recipe_data = response.POST
        recipe_file = response.FILES.get('recipe_file')
        RecipeModel.objects.create(recipe_name = recipe_data['recipe_name'],
                                 recipe_description=recipe_data['recilpe_desc'],
                                 recipe_file=recipe_file)
        return redirect('/recipes')
    
        
    
    return render(response, 'recipes.html' ,context={'PageTitle':page_title})

def explore_recipe(request):
    recipes_data = RecipeModel.objects.all()
    page_title = 'Explore Recipe'

    if request.GET.get('search'):
        recipes_data = RecipeModel.objects.filter(recipe_name__icontains = request.GET.get('search'))

    return render(request, 'explore_recipe.html', context={'recipes':recipes_data, 'PageTitle':page_title,  'data_len': len(recipes_data)})

def delete_recipe(request, id):
    recipe_data = RecipeModel.objects.filter(id=id)
    recipe_data.delete()
    return redirect('/explore_recipe')

def update_recipe(response, id):
    if response.method == 'POST':
        post_data = response.POST
        filtered_data = RecipeModel.objects.get(id=id)        
        
        filtered_data.recipe_name = post_data['recipe_name']
        filtered_data.recipe_description=post_data['recilpe_desc']
        
        if response.FILES.get('recipe_file') != None:
            post_file = response.FILES.get('recipe_file')
            filtered_data.recipe_file = post_file
        else:
            print('old files is set')
            
        filtered_data.save()
        return redirect(f'/update_recipe/{id}')
            
    recipe_data = RecipeModel.objects.get(id=id)
    print(recipe_data.recipe_description)
    return render(response, 'update_recipe.html', context={'recipes':recipe_data,})
    

def login_page(response):
    if response.method == 'POST':
        user_name = response.POST.get('user_name')
        user_pass = response.POST.get('password')
        user_name_filter = User.objects.filter(username=user_name)

        if not user_name_filter.exists():
            messages.info(response, 'Username Does\'t Exist.')
            return redirect('/login')
        else:
            user_cred = authenticate(username=user_name, password=user_pass)
            if user_cred:
                login(response, user_cred)
                return redirect('/')
            else:
                messages.info(response, 'incorrect password')
                return redirect('/login')
    return render(response, 'login.html')

def register(response):
    if response.method == 'POST':

        user = User.objects.filter(username=response.POST['user_name'])

        if user.exists():
            messages.info(response, 'Username Already Taken')
            return redirect("/register")

        user = User.objects.create(
                username= response.POST['user_name'],
                first_name= response.POST['first_name'],
                last_name= response.POST['last_name'],
                email= response.POST['email'],                
        )

        user.set_password(response.POST['password'])
        user.save()
        return redirect('/login')
    return render(response, 'register.html')

def logout_page(request):
    logout(request)
    return redirect('/')