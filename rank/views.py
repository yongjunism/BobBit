from bbuser.models import User
from django.shortcuts import render


def ranking(request):
    ranking_object = User.objects.order_by('-point')[:10]
    return render(request, 'rank/ranking.html', {'ranking_object': ranking_object})
