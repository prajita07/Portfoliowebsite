from django.shortcuts import render, redirect
from blog.models import Blog, BlogCategory
from blog.forms import BlogModelForm


def list_adminblog(request):
      if request.method =='GET':  
          blogs = Blog.objects.all()
          new_blogs = Blog.objects.all().order_by('-created_at')
          context = {   
            'blogs' : blogs,
            'new_blogs' : new_blogs,
            'categories': BlogCategory.objects.all()
            }
          return render(request, 'admin/admin_blog/admin_blog.html', context)
      else:
            blogs = Blog.objects.filter(category__id=request.POST.get('blog-category'))
            context  = {
              'filtered_blogs': blogs,
              'categories': BlogCategory.objects.all(),
              'blogcat': BlogCategory.objects.get(id=request.POST.get('blog-category'))
              }
            return render(request, 'admin/admin_blog/admin_blog.html', context)
def add_adminblog(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BlogModelForm()
        else:
            addBlog = Blog.objects.get(pk=id)
            form = BlogModelForm(instance=addBlog)
        return render(request,"admin/admin_blog/add_adminblog.html", {'form':form})
    else:
        if id == 0:
            form = BlogModelForm(request.POST, request.FILES)
        else:
            addBlog = Blog.objects.get(pk=id)
            form = BlogModelForm(request.POST,request.FILES, instance = addBlog)
        if form.is_valid():
            form.save()
        return redirect('list_adminblog')

def search_adminblog(request):
      if request.method == 'POST':
            blogs = Blog.objects.filter(title__icontains=request.POST.get('search'))
            context ={
              'results':blogs,
              'search':request.POST.get('search')
            
            }
            return render(request, 'admin/admin_blog/admin_blog.html', context)
      return redirect('list_adminblog')

def detail_admin_blog(request, id):
  if request.method == "GET" :
    blog = Blog.objects.get(id=id)
    context = {
      'blog' : blog,
    }
    return render(request,'admin/admin_blog/detail_blog.html', context)

def admin_delete_blog(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('list_adminblog')