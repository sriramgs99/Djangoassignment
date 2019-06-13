from django import forms
from .models import Post

class Postform(forms.ModelForm):
	class Meta:
		model=Post
		fields=['name','email','phone','video','image',]