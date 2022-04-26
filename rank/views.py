from bbuser.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
import json
from django.core import serializers

def ranking(request):
    ranking_object = User.objects.order_by('-point')[:10]
    return render(request, 'rank/ranking.html', {'ranking_object': ranking_object})   


# def get_ranking_list(request):
#     ranking_list = Ranking.objects.order_by('point')[:10]
#     ranking_data = serializers.serialize("json",ranking_list, fields=('nickname','point'))
#     ranking_data = json.loads(ranking_data)
#     ranking_data = [{**item['fields'],**{"pk" : item['pk']}} for item in ranking_data]
#     ranking_data = {
#         "data" : ranking_data
#     }
#     return JsonResponse(ranking_data)

# Create your views here.
# def ranking_list(request):
#     ranking_object = Ranking.objects.order_by('-point')[:10]
#     return render(request, 'rank/rank.html', {'ranking_object': ranking_object})   