from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.views.generic.edit import CreateView, DeleteView
from book_app.forms import UserForm, SellForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Sell, Cart


# Create your views here.

def home(request):
    return render(request,'home.html')

class sign_up(CreateView):
    template_name="sign_up.html"
    form_class=UserForm
    success_url=reverse_lazy("home")

    def form_valid(self,form):
        valid = super().form_valid(form)
        email = form.cleaned_data.get('email')
        username = email.split('@')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username=username[0],email=email,password=password)
        user.save()
        login(self.request, user)
        return valid

def loginpage(request):
    form = AuthenticationForm(request.POST)
    if request.method=='POST':
        username=request.POST['username'].split('@')
        password=request.POST['password']
        user=authenticate(username=username[0],password=password)
        if user is not None:
            login(request, user)
            return render(request,'home.html')
    return render(request,'login.html',{'form':form})


def logoutpage(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


def sellformcreated(request):
    return render(request,'sellformcreated.html')


def sell(request):
    if request.method == 'POST':
        form = SellForm(request.POST, request.FILES)
        if form.is_valid():
            ans = form.save(commit = False)
            # ans.owner_id = request.user.id
            ans.owner=request.user
            ans.save()
            return redirect("sellformcreated")
    return render(request,'sellform.html',{'form': SellForm()})


def borrow(request):
    books=Sell.objects.all()
    return render(request,'borrow.html',{'books':books})


def book_detail(request, uuid):
    books=Sell.objects.filter(id=uuid)
    return render(request,'book_detail.html',{'books':books})


def cartss(request):
    items = Cart.objects.all()
    return render(request, 'my_cart.html', {'books': items})


def add_to_cart(request,uuid):
    x = Cart.objects.filter(seller_id=uuid).count()
    if x:
        pass
    else:
        item = get_object_or_404(Sell, pk=uuid)
        obj = Cart(seller=item)
        obj.save()
    samaan = Cart.objects.all()
    return render(request, 'my_cart.html', {'books': samaan})


class delete_from_cart(DeleteView):
    model = Cart
    success_url = reverse_lazy('cartss')


def search(request):
    query = request.GET.get('search')
    books = Sell.objects.filter(book_name__icontains=query)
    print(books)
    return render(request, 'borrow.html', {'books':books})

def ads(request):
    items = Sell.objects.filter(owner=request.user)
    return render(request, 'borrow.html', {'books':items})

