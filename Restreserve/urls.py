"""Restreserve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from restapp import views
from django.contrib.auth import views as auth
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('register/',views.register,name='register'),
    path('login/',views.Login,name='login'),
    path('ownerhome/',views.ownerhome,name="ownerhome"),
    path('userhome/',views.userhome,name="userhome"),
    path('logout/',auth.LogoutView.as_view(template_name = 'index.html'),name="logout"),
    path('bookingstatus/',views.bookingstatus,name='bookingstatus'),
    path('bookingstatus-user/',views.bookingstatus_for_user, name='bookingstatus_for_user_url'),
    path('contact/',views.contact,name='contact'),
    path('delete/<int:id>',views.delete),
    path('delete1/<int:id>',views.delete1),
    path('delete2/<int:id>',views.delete2),
    path('edit/<int:id>',views.update, name="edit_url"),
    path('update/<int:id>',views.edit),


    path('Details',views.Details,name='Details'),
    path('Addrestdetails',views.Addrestdetails,name='Addrestdetails'),
    # path('editdetails',views.editdetails,name='editdetails'),

]
