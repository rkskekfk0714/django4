from csv import writer
from email import message
from django.shortcuts import redirect, render

from board.models import Board, Reply
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.

# 좋아요 취소
def unlikey(req,bpk):
    b = Board.objects.get(id=bpk)    
    b.likey.remove(req.user)
    return redirect("board:detail", bpk)


# 좋아요
def likey(req,bpk):
    b = Board.objects.get(id=bpk)
    b.likey.add(req.user)
    return redirect("board:detail", bpk)



# 댓글삭제
def dreply(req,bpk,rpk):
    r = Reply.objects.get(id=rpk)
    if r.replyer == req.user:
        r.delete()
    else:
        messages.error(req, "댓글을 삭제하시겠습니까?")
        return redirect("board:index")
    return redirect("board:detail", bpk)



# 댓글작성
def creply(req,bpk):
    b = Board.objects.get(id=bpk)
    c = req.POST.get("te")
    Reply(board=b, comment=c, replyer=req.user).save()
    return redirect("board:detail", bpk)


def update(req,bpk):
    b = Board.objects.get(id=bpk)

    if b.writer != req.user:
        #  협박
        return redirect("board:index")
    
    if req.method == "POST":
        us = req.POST.get("sub")
        uc = req.POST.get("con")
        b.subject = us
        b.content = uc
        b.save()
        return redirect("board:detail", bpk)
    context = {
        "b" : b
    }
    return render(req, "board/update.html", context)


def create(req):
    if req.method == "POST":        
        us = req.POST.get("usub")
        uc = req.POST.get("ucon")
        Board(subject=us, writer=req.user, content=uc, pubdate=timezone.now()).save()
        return redirect("board:index")
    return render(req, "board/create.html")


def delete(req,bpk):
    b = Board.objects.get(id=bpk)
    if b.writer == req.user:
        b.delete()
    else:
        messages.error(req, "정말 삭제하시겠습니까?")
    return redirect("board:index")


def detail(req,bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()
    context = {
        "b" : b,
        "rset" : r
    }
    return render(req, "board/detail.html", context)



def index(req):
    page = req.GET.get("page", 1)
    
    
    sel = req.GET.get("sel", "")
    tex = req.GET.get("tex", "")
    

    if tex:
        if sel == "tit":
            b = Board.objects.filter(subject__startswith=tex)
        elif sel == "wri":
            try:
                from acc.models import User
                u = User.objects.get(username=tex)
                b = Board.objects.filter(writer=u)
            except:
                b = Board.objects.none()    # 아무것도 없는 레코드라는 뜻
        elif sel == "con":
            b = Board.objects.filter(content__contains=tex)
        else:
            b = Board.objects.all()
    else:    
        b = Board.objects.all()
    
    pag = Paginator(b, 5)
    obj = pag.get_page(page)


    context = {
        "bset" : obj,
        "sel" : sel,
        "tex" : tex
    }
    
    return render(req,"board/index.html", context)