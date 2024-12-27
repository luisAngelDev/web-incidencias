from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import IncidentForm
from .models import Incident
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('incidents')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Username already exists'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })
    
@login_required
def incidents(request):
    incidents = Incident.objects.filter(fecha_solucion__isnull=True)
    return render(request, 'incidents.html', {
        'incidents': incidents
    })

@login_required
def incidents_completed(request):
    incidents = Incident.objects.filter(fecha_solucion__isnull=False).order_by('-fecha_solucion')
    return render(request, 'incidents.html', {
        'incidents': incidents
    })

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        print(request.POST)
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('incidents')
        

@login_required
def create_incident(request):

    if request.method == 'GET':
        return render(request, 'create_incident.html', {
            'form': IncidentForm
        })
    else:
        try:
            form = IncidentForm(request.POST)
            new_incident = form.save(commit=False)
            new_incident.user = request.user
            new_incident.save()
            return redirect('incidents')
        except ValueError:
            return render(request, 'create_incident.html', {
                'form': IncidentForm,
                'error': 'please provide validate data'
            })

@login_required
def incident_detail(request, incident_id):
    if request.method == 'GET':
        incident = get_object_or_404(Incident, pk=incident_id)
        form = IncidentForm(instance=incident)
        return render(request, 'incident_detail.html', {
            'incident': incident,
            'form': form
        })
    else:
        try:
            print(request.POST)
            incident = get_object_or_404(Incident, pk=incident_id)
            form = IncidentForm(request.POST, instance=incident)
            form.save()
            return redirect('incidents')
        except ValueError:
            return render(request, 'incident_detail.html', {
            'incident': incident,
            'form': form,
            'error': 'error updating incidents'
        })

@login_required
def complete_incident(request, incident_id):
    incident = get_object_or_404(Incident, pk = incident_id)
    if request.method == 'POST':
        incident.fecha_solucion = timezone.now()
        incident.revisado_por = request.user.username
        incident.save()
        return redirect('incidents')