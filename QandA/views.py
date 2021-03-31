from django.shortcuts import render
from .models import QandA
from .forms import QandAForm
from django.shortcuts import render, redirect

# Create your views here.

def QandA_write(request):
    if request.method == 'POST':
        form = QandAForm(request.POST)
        if form.is_valid():
            qanda = QandA() 
            
            email_user = form.cleaned_data['email_user']
            email_site = form.cleaned_data['email_site']
            phone_first = form.cleaned_data['phone_first']
            phone_middle = form.cleaned_data['phone_middle']
            phone_last = form.cleaned_data['phone_last']
            fax_first = form.cleaned_data['fax_first']
            fax_middle = form.cleaned_data['fax_middle']
            fax_last = form.cleaned_data['fax_last']


            qanda.writer = form.cleaned_data['writer']
            qanda.company = form.cleaned_data['company']
            qanda.email = email_user + '@' + email_site
            qanda.phone = phone_first + '-' + phone_middle + '-' + phone_last
            qanda.fax = fax_first + '-' + fax_middle + '-' + fax_last
            qanda.title = form.cleaned_data['title']
            qanda.content = form.cleaned_data['content']
            qanda.save()

            return redirect('/qanda/')
    else:
        form = QandAForm()
    return render(request, 'qanda.html', {'form': form})

    
def personal_info(request):
    return render(request, '(주)해강기술개인정보처리방침.html')