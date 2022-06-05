from django.shortcuts import redirect, render
from .models import Book
# Create your views here.

def create(req):
    if req.method == "POST":
        a = req.POST.get("impo")
        b = req.POST.get("sn")
        c = req.POST.get("su")
        d = req.POST.get("scon")
        Book(site_name=b, site_url=c, site_con=d, maker=req.user, impo=bool(a)).save()
        return redirect("book:index")
    return render(req, "book/create.html")


def index(req):
    b = req.user.book_set.all()
    context = {
        "bset" : b
    }
    return render(req, "book/index.html", context)