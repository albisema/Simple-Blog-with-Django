from django.shortcuts import render, HttpResponseRedirect
from .forms import AddBlogPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required

@login_required
def blogForm(request):
    form = AddBlogPostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.title :
            instance.title = 'Untitled Post'
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect('/blog/posts/')

    context = {
        'form': form,
    }

    return render(request, 'blog/form.html', context)

def viewPosts(request):
    list = BlogPost.objects.all()
    context = {
        'list': list
    }
    return render(request, 'blog/posts.html', context)