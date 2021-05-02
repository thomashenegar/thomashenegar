from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):  
    def register_validator(self, postData):
        errors={}
        if len(postData['first_name'])<2:
            errors['first_name']="First name must be at least 2 characters."
        if len(postData['last_name'])<2:
            errors['last_name']="Last name must be at least 2 characters."
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = "Invalid email address!"
        if len(postData['password'])<8:
            errors['password']="Password must be 8 characters long."
        if postData['password']!=postData['confirm_password']:
            errors['confirm_password']="Password and confirmation password must match."
        return errors
    def login_validator(self, postData):
        errors={}
        user=User.objects.filter(email=postData['user_email'])
        if len(user)<1:
            errors['user_email']="Invalid Credentials."
        else:
            logged_user=user[0]
            if not bcrypt.checkpw(postData['user_password'].encode(), logged_user.password.encode()):
                errors['user_email']="Invalid Credentials."
        return errors

class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=15)

    created_at=models.DateTimeField(auto_now_add=True)
    upated_at=models.DateTimeField (auto_now=True)
    objects=UserManager()
