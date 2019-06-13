from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,CreateView
from .forms import Postform
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


class Viewall(ListView):
	model=Post
	template_name='blog/viewall.html'
	context_object_name = 'posts'
	

class Register(CreateView):
	model=Post
	form_class=Postform
	queryset=Post.objects.all()
	template_name='blog/post_form.html'
	success_url = reverse_lazy('blog-home')
