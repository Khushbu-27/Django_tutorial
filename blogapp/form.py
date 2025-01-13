
from django import forms
from .models import Post

class BlogForm(forms.ModelForm):
    
    class Meta:
        
        model = Post
        fields = ['title', 'content'] 
        odering = ['-date_posted']
