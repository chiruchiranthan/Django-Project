"""gift URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from store.views import Home,Gift_type,Showpieces,Stationary,Electronics,Books,Dolls,Addorder,Gift,Buy,About,Contact,Signup,Login
from store.views import GiftListView,DollsListView,ShowListView,ElecListView,StatListView
from store.views import simple_upload,model_form_upload
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from store import views
from store.views import contact

urlpatterns = [
    path("logout/", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path('admin/', admin.site.urls),
    path('home/',Home),
    path('gifttype/', Gift_type),
    path('showpieces/', Showpieces),
    path('stationary/', Stationary),
    path('electronics/', Electronics),
    path('books/', Books),
    path('dolls/',Dolls),
    path('buy/', Buy),
    path('addorder/', Addorder),
    path('signup/', Signup),
    path('lg/',Login),
    path('gift/', Gift),
    path('about/', About),
    path('su/',simple_upload),
    path("up/",model_form_upload),
    path('giftlist/',GiftListView.as_view()),
    path('dollslist/',DollsListView.as_view()),  
    path('statlist/',StatListView.as_view()),
    path('eleclist/',ElecListView.as_view()),
    path('showlist/',ShowListView.as_view()),
    path('contact/',contact)
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()