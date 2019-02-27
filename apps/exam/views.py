from django.shortcuts import render, redirect, HttpResponse
from .models import User, Quote
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, "exam/index.html")

def registration_process(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    else:
        hash_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create( first_name=request.POST['first_name'], 
                                        last_name=request.POST['last_name'], 
                                        email=request.POST['email'], 
                                        password=hash_password.decode())
        request.session["user_id"] = new_user.id
        request.session["f_name"] = new_user.first_name
        request.session["l_name"] = new_user.last_name
        return redirect("/quotes")

def login_process(request):
    # if request.method=='post'

    errors =User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        logged_in_user = User.objects.get(email=request.POST["login_email"])
        request.session["user_id"] = logged_in_user.id
        request.session["f_name"] = logged_in_user.first_name
        request.session["l_name"] = logged_in_user.last_name
        return redirect('/quotes')
    

def quotes(request):
    if 'user_id' not in request.session:
        return redirect('/')
    # x = Quote.objects.get(id=1)
    context = {
        'logInInfo' : User.objects.get(id = request.session['user_id']),
        'messageList' : Quote.objects.all().order_by('-created_at')
    }
    # print(x.author)
    return render(request, 'exam/welcome.html', context)

def post_quote(request):
    errors =Quote.objects.quote_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quotes')
    else:
        user= User.objects.get(id = request.session['user_id'])
        Quote.objects.create(author = request.POST['author'],
                            quote=request.POST['quote_post'],
                            user=user)
    return redirect('/quotes')

# def post_likes(request):
#     user = User.objects.get(id= request.session['user_id'])
    
#     Like.objects.create( quote_like= request.POST['like_button'], 
#                             )
#     return redirect('/quotes')

def user_page(request, id):
    context = {
        "user" : User.objects.get(id=id),
        "user_dashboard" : User.objects.get(id=id).quotes.all()
        # "user_quotes": Quote.objects.get(id=id),
    } 
    return render(request, "exam/user_page.html", context)

def myaccount(request):
    return render(request, "exam/myaccount.html")

def update(request):
    errors = User.objects.account_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/myaccount")

    else:
        new_user = User.objects.create(first_name=request.POST['fn'], 
                                        last_name=request.POST['ln'], 
                                        email=request.POST['em'],)
        new_user.save()

        return redirect("/quotes")

def log_off(request):
    request.session.flush()
    return redirect('/')