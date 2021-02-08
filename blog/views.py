from django.shortcuts import render, redirect
from . models import Blog, BlogCategory
from .forms import BlogModelForm
def list_blog(request):
    if request.method =='GET':  
        blogs = Blog.objects.all()
        new_blogs = Blog.objects.all().order_by('-created_at')
        
        context = {
            'blogs': blogs,
            'new_blogs':new_blogs,
            'categories':BlogCategory.objects.all()
        }
        return render(request, 'blog/list.html', context)
    else:
         blogs = Blog.objects.filter(category__id=request.POST.get('blog-category'))
         context  = {
           'filtered_blogs': blogs,
           'categories':BlogCategory.objects.all(),
           'blogcat':BlogCategory.objects.get(id=request.POST.get('blog-category'))
         }
         return render(request, 'blog/list.html', context)

def search_blog(request):
    if request.method == 'POST':
        results = Blog.objects.filter(title__icontains=request.POST.get('search'))
        context ={
        'results':results,
        'search':request.POST.get('search')
        }

        return render(request,"blog/list.html", context)
    return redirect('list_blog')

def add_blog(request):
  if request.method == 'POST':
    form= BlogModelForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('list_blog')
  else:
      form= BlogModelForm()
  return render (request, 'blog/add_blog.html', {'form':form})
  