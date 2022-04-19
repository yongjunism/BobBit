from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class TestView(TemplateView):
    template_name = "bbuser/test.html"


def TestView2():
    context = {}
    return render(context=context)
