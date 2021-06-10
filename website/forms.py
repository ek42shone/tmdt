from django.forms import ModelForm

from staff.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']