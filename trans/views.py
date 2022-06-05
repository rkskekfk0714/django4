from asyncio import Transport
from googletrans import Translator
from django.shortcuts import render
import googletrans


# Create your views here.


def index(req):
    # d = googletrans.LANGUAGES

    # text1 = req.POST.get("h")
    # t = Translator()

    # # for i in d:
    # #     trans1 = t.translate(text1, src='en', dest=i)

    # context = {
    #     "dset" : d,
    #     # "trans1" : trans1
    # }

    context = {
        "nd" : googletrans.LANGUAGES
        
    }

    if req.method == "POST":
        b = req.POST.get("bf")
        f = req.POST.get("sel1")
        t = req.POST.get("sel2")
        trans = Translator()
        a = trans.translate(b, src=f, dest=t)
        context.update({
            "af" : a.text,
            "fr" : f,
            "to" : t,
            "bf" : b
        })
    return render(req,"trans/index.html", context)