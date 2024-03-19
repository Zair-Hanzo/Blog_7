from django.shortcuts import render, redirect

from .models import BlogPost, BlogText

from .forms import BlogPostForm, BlogTextForm

# Create your views here.

def home(request):
    return render(request, 'blogs/home.html')

def blogposts(request):
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/blogposts.html', context)

def blogpost(request, blogpost_id):
    blogpost = BlogPost.objects.get(id=blogpost_id)
    blogtexts = blogpost.blogtext_set.order_by('-date_added')
    context = {'blogpost': blogpost, 'blogtexts': blogtexts}
    return render(request, 'blogs/blogpost.html', context)

def new_blogpost(request):
    """ Add a new blogpost """
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogposts')
        
    context = {'form': form}
    return render(request, 'blogs/new_blogpost.html', context)

def new_blogtext(request, blogpost_id):
    blogpost = BlogPost.objects.get(id=blogpost_id)

    if request.method != 'POST':
        form = BlogTextForm()
    else:
        form = BlogTextForm(data=request.POST)
        if form.is_valid():
            new_blogtext = form.save(commit=False)
            new_blogtext.blogpost = blogpost
            new_blogtext.save()
            return redirect('blogs:blogpost', blogpost_id=blogpost_id)

    context = {'form': form, 'blogpost': blogpost}
    return render(request, 'blogs/new_blogtext.html', context)    

def edit_blogtext(request, blogtext_id):
    blogtext = BlogText.objects.get(id=blogtext_id)
    blogpost = blogtext.blogpost

    if request.method != "POST":
        # Initial request, pre-fill form with the current blogtext
        form = BlogTextForm(instance=blogtext)
    else:
        form = BlogTextForm(instance=blogtext, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogpost', blogpost_id=blogpost.id)
    
    context = {'form': form, 'blogtext': blogtext, 'blogpost': blogpost}
    return render(request, 'blogs/edit_blogtext.html', context)
