from django import forms

class QandAForm(forms.Form):
    writer = forms.CharField(
        error_messages={
            'required': '작성자를 입력하세요.'
        },
        max_length=128, label="작성자")
    company = forms.CharField(
        error_messages={
            'required': '회사명을 입력하세요.'
        },
        max_length=256, label="회사명")

    email_user = forms.CharField(
        error_messages={
            'required': '이메일을 입력하세요.'
        },
        max_length=256, label="이메일")

    email_site = forms.CharField(
        error_messages={
            'required': '이메일을 입력하세요.'
        },
        max_length=256, label="이메일")

    phone_first= forms.CharField(
        error_messages={
            'required': '전화번호를 입력하세요.'
        },
        max_length=256, label="전화번호")
    
    phone_middle= forms.CharField(
        error_messages={
            'required': '전화번호를 입력하세요.'
        },
        max_length=256, label="전화번호")
    
    phone_last= forms.CharField(
        error_messages={
            'required': '전화번호를 입력하세요.'
        },
        max_length=256, label="전화번호")

    fax_first = forms.CharField(required=False, max_length=256, label="팩스번호")
    fax_middle = forms.CharField(required=False, max_length=256, label="팩스번호")
    fax_last = forms.CharField(required=False, max_length=256, label="팩스번호")
    title = forms.CharField(
        error_messages={        
            'required': '제목을 입력하세요.'
        },
        max_length=128, label="제목")
    content = forms.CharField(
        error_messages={
            'required': '내용을 입력하세요.'
        },
        widget=forms.Textarea, label="내용") # widget=forms.Textarea : 입력이 텍스트에어리어 형태로..