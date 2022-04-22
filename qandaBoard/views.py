from re import U
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth.decorators import login_required
from django.db import transaction
from datetime import datetime
from django.shortcuts import render, redirect

#게시판 리스트
@login_required
def index(request):
    #페이징
    page = request.GET.get('page', '1')  # 페이지
    #boards = {'boards': Board.objects.all().order_by('-board_reg_date')}
    boards = Board.objects.filter(board_deleted='N').order_by('-board_reg_date')
    # 페이징처리
    paginator = Paginator(boards, 7)  # 페이지당 7개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'boards': page_obj}
    return render(request, 'qandaBoard/list.html', context)

#질문 남기기   
from .models import Board,User
from django.contrib.auth import get_user_model
def post(request):
    try:
        if request.method == "POST":
            board_title = request.POST['board_title']
            board_content = request.POST['board_content']
            User = get_user_model()
            user = get_object_or_404(User, username=request.user)
            board = Board(
                board_title=board_title, 
                board_content=board_content, 
                board_reg_date = datetime.now(),
                user = user
                )
            board.save()
            return redirect('/qna')
        else:
            return render(request, 'qandaBoard/post.html')
    except:
        return HttpResponseRedirect(content='404 NOT FOUND')

#질문 상세 조회
from django.http import HttpResponseRedirect, Http404
def detail(request, post_id):
    try:
        board = Board.objects.get(pk=post_id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'qandaBoard/detail.html', {'board': board})