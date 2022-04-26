from re import U
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Board,User
from django.contrib.auth import get_user_model
from .forms import * 

#게시판 리스트
@login_required
def index(request):
    #페이징
    page = request.GET.get('page', '1')  # 페이지
    #boards = {'boards': Board.objects.all().order_by('-board_reg_date')}
    boards = Board.objects.filter(board_deleted='N').order_by('-board_reg_date')
    replys = Reply.objects.filter(reply_deleted='N')
    replycnt = replys.count()
    # 페이징처리
    paginator = Paginator(boards, 7)  # 페이지당 7개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'boards': page_obj, 'replycnt' : replycnt}
    return render(request, 'qandaBoard/list.html', context)

#질문 남기기   
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


def detail(request, post_id):
    #form 처리
    if request.method == 'POST':
        if 'reply_content' in request.POST:
            form = ReplyForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data['reply_content']
                uid = form.data['user_id']
                bid = form.data['board_id']
                Reply.objects.create(reply_content=content, reply_deleted = 'N', user_id = uid, board_id = bid)
                return redirect('/detail/'+form.data['board_id'])
            else:
                return redirect('/detail/'+form.data['board_id'])
        else:
            form = DeleteBoardForm(request.POST)
            b_id = form.data['id']
            if form.data['delete_YN'] == 'Y':
                b = Board.objects.get(board_id = b_id)
                b.board_deleted = 'Y'
                b.save()
                return redirect('/qna')
    try:
        board = Board.objects.get(pk=post_id)
    except:
        return HttpResponseNotFound(content='404 NOT FOUND')
    if board.board_deleted == 'Y':
        return HttpResponseNotFound(content='404 NOT FOUND')
    replys = Reply.objects.filter(reply_deleted='N',board_id=board.board_id)
    formreply = ReplyForm()
    formdelete = DeleteBoardForm()
    # user = User.objects.get(id = board.user.id)
    User = get_user_model()
    user = get_object_or_404(User, username=request.user)
    board.save()
    print(request.GET.get)
    return render(request, 'qandaBoard/detail.html',
    {'board':board, 'replys':replys,'user':user,'formdelete':formdelete, 'formreply':formreply })

