from django.shortcuts import render
from .models import Noticeboard, Referenceboard
from django.views.generic import ListView, DeleteView

# Create your views here.

class NoticeList(ListView):
    model = Noticeboard
    template_name = 'notice.html'
    context_object_name = 'post_list'
    paginate_by = 3

class ReferenceList(ListView):
    model = Referenceboard
    template_name = 'reference.html'
    context_object_name = 'post_list'

class NoticeboardDetail(DeleteView):
    template_name = "notice_board_detail.html"
    queryset = Noticeboard.objects.all()
    context_object_name = 'board'

class ReferenceboardDetail(DeleteView):
    template_name = "reference_board_detail.html"
    queryset = Referenceboard.objects.all()
    context_object_name = 'board'