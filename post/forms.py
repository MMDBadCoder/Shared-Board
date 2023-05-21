from django.forms import ModelForm

from post.models import MyPost


class PostForm(ModelForm):
    class Meta:
        model = MyPost
        fields = ['text', 'file']
