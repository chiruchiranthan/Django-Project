from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from store.forms import OrderForm,DocumentForm,SignupForm,LoginForm,NewUserForm
from store.models import gift
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from store.contact import ContactForm

# Create your views here.
def Home(request):
   return render(request,"home.html")
def Gift(request):
   return render_to_response("gift.html")
def Gift_type(request):
    return render_to_response("gifttype.html")
def Dolls(request):
    return render_to_response("dolls.html") 
def Stationary(request):
    return render_to_response("stationary.html") 
def Books(request):
    return render_to_response("books.html") 
def Electronics(request):
    return render_to_response("electronics.html")
def Showpieces(request):
    return render_to_response("showpieces.html") 
    return render_to_response("electronics.html")
def Buy(request):
    return render_to_response("buy.html") 
def About(request):
    return render_to_response("about.html") 
def Contact(request):
    return render_to_response("contact.html") 

def contact(request):
   submitted = False
   if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
         cd = form.cleaned_data
         # assert False
         return HttpResponseRedirect('/contact?submitted=True')
   else:
      form = ContactForm()
      if 'submitted' in request.GET:
         submitted = True
   return render(request, 'contact.html', {'form': form, 'submitted':submitted})


def Addorder(request):
   submitted = False
   if request.method == 'POST':
      form = OrderForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/addorder/?submitted=True')
   else:
      form = OrderForm()
      if 'submitted' in request.GET:
         submitted = True
   return render(request, 'addorder.html', {'form': form, 'submitted':submitted})

def Signup(request):
   submitted = False
   if request.method == 'POST':
      form = SignupForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/home/?submitted=True')
   else:
      form = SignupForm()
      if 'submitted' in request.GET:
         submitted = True
   return render(request, 'Addcustomer.html', {'form': form, 'submitted':submitted})

def Login(request):
   submitted = False
   if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/home/?submitted=True')
   else:
      form = LoginForm()
      if 'submitted' in request.GET:
         submitted = True
   return render(request, 'login.html', {'form': form, 'submitted':submitted})

class GiftListView(generic.ListView):
   model = gift
   template_name = 'gift_list.html'

class DollsListView(generic.ListView):
   model = gift
   template_name = 'dolls_list.html'


class StatListView(generic.ListView):
   model = gift
   template_name = 'stat_list.html'


class ElecListView(generic.ListView):
   model = gift
   template_name = 'elec_list.html'


class ShowListView(generic.ListView):
   model = gift
   template_name = 'show_list.html'

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('Customer_name')
            password = form.cleaned_data.get('Password')
            user = authenticate(Customer_name=username, Password=password)
            if user is not None:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'supl.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'supl.html') 

def model_form_upload(request):
   if request.method == 'POST':
      form = DocumentForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('/up')
   else:
      form = DocumentForm()
   return render(request, 'model_form_upload.html', {'form': form})




