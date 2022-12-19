from .models import Comment
from django import forms


# Form for creating and updating comments
class CommentForm(forms.ModelForm):
    class Meta:
        # Use the Comment model to create the form fields
        model = Comment
        # Only include the body field in the form
        fields = ('body',)
