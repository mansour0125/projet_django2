"""
URL configuration for ISEPAT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Etudiant.views import liste_apprenants, detail_apprenant, ajout_apprenant, modification_apprenant, supprimer_apprenant,login_view,signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', liste_apprenants, name='liste_apprenants'),
    path('detail_apprenant/<int:id>/', detail_apprenant, name='detail_apprenant'),
    path('ajout_apprenant/', ajout_apprenant, name='ajout_apprenant'),
    path('modification_apprenant/<int:id>/', modification_apprenant, name='modification_apprenant'),
    path('supprimer_apprenant/<int:id>/', supprimer_apprenant, name='supprimer_apprenant'),
    path('login/', login_view, name='login'),
     path('signup/', signup, name='signup'),
]