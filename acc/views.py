from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from acc.models import User
from django.contrib import messages
# Create your views here.

def delete(req):
    pw = req.POST.get("pwck")
    if check_password(pw, req.user.password):
        req.user.pic.delete()
        req.user.delete()
        return redirect("acc:index")
    else:
        messages.info(req, "패스워드가 일치하지 않습니다.")
        return redirect("acc:profile")


def update(req):
    if req.method == "POST":
        u = req.user
        up = req.POST.get("upass")
        ua = req.POST.get("uage")
        ue = req.POST.get("umail")
        uc = req.POST.get("ucomm")
        upi =  req.FILES.get("upic")
        if upi:
            u.pic.delete()
            u.pic = upi
        if up:
            u.set_password(up)
        u.comment = uc
        u.age = ua
        u.email = ue
        u.save()
        login(req, u)
        return redirect("acc:profile")
    return render(req,"acc/update.html")



def signup(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        uc = req.POST.get("ucomm")
        upi =  req.FILES.get("upic")
        try:
            User.objects.create_user(username=un, password=up, comment=uc, pic=upi)
            return redirect("acc:login")
        except:       
            messages.info(req, "USERNAME 이 중복되어 계정이 생성되지 않았습니다.")
    return render(req, "acc/signup.html")


def profile(req):
    return render(req,"acc/profile.html")

def logout_user(req):
    logout(req)
    return redirect("acc:index")

def login_user(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(req, u)
            messages.success(req, f"{u}!! WELCOME~")
            return redirect("acc:index")
        else:
            messages.error(req, "계정정보가 일치하지 않습니다.")
    return render(req,"acc/login.html")

def index(req):
    return render(req,"acc/index.html")