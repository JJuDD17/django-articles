from django import forms

class ArticleForm(forms.Form):
    author_name = forms.CharField(label='Your name', empty_value='Somebody', max_length=32)
    title = forms.CharField(label='Article title', empty_value='Title', max_length=120)
    article_text = forms.CharField(label='Article text', max_length=5000)