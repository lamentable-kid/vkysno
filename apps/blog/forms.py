from django import forms

from apps.blog.models import Comment


class CommentFormForRegistered(forms.ModelForm):
    is_checked = False

    class Meta:
        model = Comment
        fields = ['username', 'email', 'text', 'is_checked']


class CommentFormForLogined(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    is_checked = True

    class Meta:
        model = Comment
        fields = ['username', 'email', 'text', 'is_checked']
