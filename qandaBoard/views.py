from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from .models import *


# Create your views here.
def index(request):
    #페이징
    page = request.GET.get('page', '1')  # 페이지
    #boards = {'boards': Board.objects.all().order_by('-board_reg_date')}
    boards = Board.objects.all().order_by('-board_reg_date')
    # 페이징처리
    paginator = Paginator(boards, 7)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'boards': page_obj}
    return render(request, 'qandaBoard/list.html', context)
    

def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'qandaBoard/post.html')