from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# ====================RENDER HOME PAGE=========================
def index(request):

    return render(request, "index.html")
# =====================PROCESS NEW ADMIN REGISTRATION===========
def register_new_admin(request):

    errors=User.objects.register_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/admin")
    else:
        hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(hash)

        new_user=User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hash,
        )

        request.session['new_user']=new_user.id

    return redirect("/admin_portal")
# ========================LOGIN CURRENT USER===================
def login_current_admin(request):

    errors=User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/admin")
    else:
        current_user=User.objects.filter(email=request.POST['user_email'])
        request.session['new_user']=current_user[0].id

    return redirect("/admin_portal")
# ========================RENDER SHOP PAGE=====================
def shop(request):

    return render(request, "shop.html")
# ====================== RENDER PRODUCT INFO PAGE==============
def product_info(request):

    return render(request, "productinfo.html")
# ========================RENDER CHECKOUT PAGE=================
def checkout(request):

    return render(request, "checkout.html")
# =========================RENDER ABOUT ME/CONTACT PAGE========
def about_me_and_contact(request):

    return render(request, "aboutmeandcontact.html")
# =========================RENDER EVENTS PAGE==================
def events(request):

    return render(request, "events.html")
# ========================RENDER ADMIN PAGE====================
def admin_login(request):

    return render(request, "adminlogin.html")
# =======================RENDER ADMIN PORTAL PAGE==============
def admin_portal(request):

    return render(request, "adminportal.html")
