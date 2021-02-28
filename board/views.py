from django.shortcuts import render
from .models import Board
from django.views.generic import ListView

# Create your views here.

class NoticeList(ListView):
    model = Board
    template_name = 'notice.html'
    context_object_name = 'post_list'

class FreeBoardList(ListView):
    model = Board
    template_name = 'freeboard.html'
    context_object_name = 'post_list'

class ReferenceList(ListView):
    model = Board
    template_name = 'reference.html'
    context_object_name = 'post_list'