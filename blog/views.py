from django.shortcuts import render, HttpResponseRedirect, redirect
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
    list = BlogPost.objects.order_by('-timestamp')
    context = {
        'list': list
    }
    return render(request, 'blog/posts.html', context)

@login_required
def delete_item(request, id):
    instance = BlogPost.objects.get(pk=id)
    if (request.user == instance.user):
        instance.delete()
    return redirect('/blog/posts/')