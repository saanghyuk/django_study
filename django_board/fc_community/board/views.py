from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Board
from django.http import Http404
from fcuser.models import Fcuser
from tag.models import Tag
from .forms import BoardForm

# Create your views here.


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다. ')
    return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login')
    if request.method == 'POST':
        form = BoardForm(request.POST)
        user_id = request.session.get('user')
        if form.is_valid():
            fcuser = Fcuser.objects.get(pk=user_id)
            tags = form.cleaned_data['tags'].split(',')
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            for tag in tags:
                if not tag:
                    continue
                # 일치하는 모델이 있으면 가지고 오고, 없으면 생성, created T/F로 나옴, 사용하지 않는 변수면 그냥 _로 씀
                _tag, _ = Tag.objects.get_or_create(name=tag)
                print(_tag)
                board.tags.add(_tag)

            return redirect('/board/list')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):

    # id의 역순으로 가지고 오겠다.
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('page', 1))
    paginator = Paginator(all_boards, 4)
    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})
