from django import forms

from apps.blog.models import Comment


class CommentFormForRegistered(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['username', 'email', 'text']


class CommentFormForLogined(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = Comment
        fields = ['username', 'email', 'text']
