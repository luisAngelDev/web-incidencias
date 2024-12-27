"""
URL configuration for djangoinsidencias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from incidents import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('incidents/', views.incidents, name='incidents'),
    path('incidents_completed/', views.incidents_completed, name='incidents_completed'),
    path('incidents/create/', views.create_incident, name='create_incident'),
    path('incidents/<int:incident_id>/', views.incident_detail, name='incident_detail'),
    path('tasks/<int:incident_id>/complete', views.complete_incident, name='complete_incident'),
    path('signin/', views.signin, name='signin'),
]