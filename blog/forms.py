from django import forms
from .models import BlogPost

class AddBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "description"]