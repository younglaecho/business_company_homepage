from django import forms
from .models import Noticeboard, Referenceboard, Comment

class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=64, label='제목'
    )
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        }, label='상품설명'
    )
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','password','content']
        labels = {
            'content': '댓글내용',
        }

# def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('name')
    #     price = cleaned_data.get('price')
    #     description = cleaned_data.get('description')
    #     stock = cleaned_data.get('stock')

    #     if name and price and description and stock:
    #         product = Product(
    #             name=name,
    #             price=price,
    #             description=description,
    #             stock=stock
    #         )
    #         product.save()