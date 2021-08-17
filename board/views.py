from django.shortcuts import render
from .models import Noticeboard, Referenceboard, Comment
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.utils import timezone
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.

class NoticeList(ListView):
    model = Noticeboard
    template_name = 'notice.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(NoticeList, self).get_context_data(**kwargs)
        page_list = range(-2, 3, 1)
        context['page_list'] = list(page_list)
        return context


class ReferenceList(ListView):
    model = Referenceboard
    template_name = 'reference.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(ReferenceList, self).get_context_data(**kwargs)
        page_list = range(-2, 3, 1)
        context['page_list'] = list(page_list)
        return context


class NoticeboardDetail(DetailView):
    template_name = "notice_board_detail.html"
    queryset = Noticeboard.objects.all()
    context_object_name = 'board'

    # def post(request, pk):
    #     notice=get_object_or_404(Noticeboard, pk=pk)
    #     if request.method == "POST":
    #         form=CommentForm(request.POST)
    #         if form.is_valid():
    #             comment=form.save(commit=False)
    #             comment.notice_comment=notice.id
    #             comment.created_date = timezone.now()
    #             comment.save()
    #             return redirect('/board')
    #     else:
    #         form=CommentForm()
    #     return render(request, 'notice_board_detail.html', {'form':form})


class ReferenceboardDetail(DetailView):
    template_name = "reference_board_detail.html"
    queryset = Referenceboard.objects.all()
    context_object_name = 'board'
