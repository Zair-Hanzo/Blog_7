from django import forms

from .models import BlogPost, BlogText

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title']
        labels = {'title': 'Fill out'}

class BlogTextForm(forms.ModelForm):
    class Meta:
        model = BlogText
        fields = ['text']
        labels = {'text': 'Text'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
