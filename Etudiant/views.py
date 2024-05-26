from django.shortcuts import render, get_object_or_404, redirect
from .models import Apprenant
from .forms import ApprenantForm,SignUpForm
from django.contrib.auth import authenticate, login
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q


def liste_apprenants(request):
    apprenants = Apprenant.objects.all()
    return render(request, 'liste_apprenants.html', {'apprenants': apprenants})

def detail_apprenant(request, id):
    apprenant = get_object_or_404(Apprenant, id=id)
    return render(request, 'detail_apprenant.html', {'apprenant': apprenant})

def ajout_apprenant(request):
    if request.method == 'POST':
        form = ApprenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_apprenants')
    else:
        form = ApprenantForm()
    return render(request, 'ajout_apprenant.html', {'form': form})

def modification_apprenant(request, id):
    apprenant = get_object_or_404(Apprenant, id=id)
    if request.method == 'POST':
        form = ApprenantForm(request.POST, instance=apprenant)
        if form.is_valid():
            form.save()
            return redirect('liste_apprenants')
    else:
        form = ApprenantForm(instance=apprenant)
    return render(request, 'modification_apprenant.html', {'form': form, 'apprenant': apprenant})

def supprimer_apprenant(request, id):
    apprenant = get_object_or_404(Apprenant, id=id)
    if request.method == 'POST':
        apprenant.delete() 
        return redirect('liste_apprenants')
    return render(request, 'supprimer_apprenants.html', {'apprenant': apprenant})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            print(user)
            login(request, user)
            return redirect('liste_apprenants')  # Rediriger vers la page d'accueil après la connexion
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':

        username = request.POST.get('username',None)
        email = request.POST.get('email',None)
        password = request.POST.get("password",None)
        password2 = request.POST.get('password2',None)

        validate_email(email)

        if password != password2:

            print('les deux mot de passe ne correspond pas') 

        user=User.objects.filter(Q(email = email) | Q(username = username)).first()
        print(user)

        if user:
            print(user)
        else:
            user = User(username = username, email = email)
            user.save()

            user.password = password
            user.set_password(user.password)
            user.save()
       
    return render(request,'signup.html')
    
