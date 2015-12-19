from django.shortcuts import render
from .forms import AddBlogPostForm

def blogForm(request):
    form = AddBlogPostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if instance.title is None:
            instance.title = 'Untitled Post'
        instance.user = request.user
        instance.save()
        form = AddBlogPostForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/form.html', context)