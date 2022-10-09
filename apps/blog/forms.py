from django import forms

from apps.blog.models import Commentariy


class CommentForm(forms.ModelForm):

    class Meta:
        model = Commentariy
        fields = '__all__'
