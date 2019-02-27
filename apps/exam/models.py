from django.db import models

# Create your models here.
from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):

    def reg_validator(self, postData):
        errors={}
        #name errors
        if len(postData["first_name"]) < 1:
            errors["first_name_error"] = "Please enter first name!"
        elif len(postData["first_name"]) < 2:
            errors["first_name_error"] ="please enter valid first name!"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["first_name"]):
            errors["first_name_error"] = "First Name should have letters only (not numbers or special characters)!"

        #last name errors
        if len(postData["last_name"]) < 1:
            errors["last_name_error"] = "Please enter last name!"
        elif len(postData["last_name"]) < 2:
            errors["last_name_error"] = "please enter a valid Last Name!"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["last_name"]):
            errors["last_name_error"] = "Last Name should have letters only (not numbers or special characters)!"
        
        #email errors
        if len(postData["email"]) < 1:
            errors["email_error"] = "Email cannot be blank!"
        elif not re.compile(r'^[a-zA-Z0-9+-_]+@[a-zA-Z0-9+-_]+.[a-zA-Z0-9+-_]$').match(postData["email"]):
            errors["email_error"] = "Please enter vaild email form (eg. abc123@gmail.com)!"
        #email already exits errors
        elif len(User.objects.filter(email=postData["email"])) > 0:
            errors["dublicate_email"] = "Email already exits. Please use new email!"

        #password errors
        if len(postData["password"]) < 3:
            errors["password_error"] ="password needs to be more than 3 characters!"
        elif postData["password"] != postData["confirm_password"]:
            errors["password_error"] = "password did not match!"

        return errors

    def login_validator(self, postDATA):
        existing = User.objects.filter(email=postDATA["login_email"])
        errors={}
        #check if the email already exists
        if len(existing)==0:
            errors["one"]="Email is not register. Please register ar first!"
        #check if the password is correct
        elif not bcrypt.checkpw(postDATA["login_password"].encode(), existing[0].password.encode()):
            errors["two"] = "password is not correct!"
        
        return errors

    def account_validator(self, postData):
        errors={}
        #name errors
        if len(postData["fn"]) < 1:
            errors["first_name_error"] = "Please enter first name!"
        elif len(postData["fn"]) < 2:
            errors["first_name_error"] ="please enter valid first name!"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["fn"]):
            errors["first_name_error"] = "First Name should have letters only (not numbers or special characters)!"

        #last name errors
        if len(postData["ln"]) < 1:
            errors["last_name_error"] = "Please enter last name!"
        elif len(postData["ln"]) < 2:
            errors["last_name_error"] = "please enter a valid Last Name!"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["ln"]):
            errors["last_name_error"] = "Last Name should have letters only (not numbers or special characters)!"
        
        #email errors
        if len(postData["em"]) < 1:
            errors["email_error"] = "Email cannot be blank!"
        elif not re.compile(r'^[a-zA-Z0-9+-_]+@[a-zA-Z0-9+-_]+.[a-zA-Z0-9+-_]$').match(postData["em"]):
            errors["email_error"] = "Please enter vaild email form (eg. abc123@gmail.com)!"
        #email already exits errors
        elif len(User.objects.filter(email=postData["em"])) > 0:
            errors["dublicate_email"] = "Email already exits. Please use new email!"
        return errors

class QuoteManager (models.Manager):
    def quote_validator(self, postDATA):
        errors={}
        #Author errors
        if len(postDATA["author"]) < 1:
            errors["author_error"] = "please enter Author's name!"
        elif len(postDATA["author"]) < 3:
            errors["author_error"] = "Author's name must be more than 3 characters!"
        #quotes errors
        if len(postDATA["quote_post"]) < 1:
            errors["quote_error"] = "please enter a quote!"
        elif len(postDATA["quote_post"]) < 10:
            errors["quote_error"] = "quote must be more than 10 characters!"
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now =True)
    #messages
    #comments
    objects = UserManager()

class Quote(models.Model):
    author = models.CharField(max_length = 255)
    quote = models.TextField()
    user = models.ForeignKey(User, related_name="quotes")
    # like = models.ForeignKey(User, related_name="likes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()
    # poster = models.ForeignKey(User, related_name ='messages')
    

# class Like(models.Model):
#     quote_like= models.ForeignKey(Quote, related_name="like_quote")
#     user_like = models.ForeignKey(User, related_name = "like_user")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)