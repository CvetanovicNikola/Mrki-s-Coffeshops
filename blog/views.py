from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic import ListView, DetailView, CreateView


class All_blogs(ListView):
    model = Blog
    context_object_name = "blogs"
    ordering = ["-date"]
    paginate_by = 3

    def get_queryset(self):

        try:
            title = self.request.GET.get('title')
        except:
            title = ""
        if title:
            objects_list = Blog.objects.filter(title__icontains=title)
        else:
            objects_list = Blog.objects.all()
        return objects_list


class Blog_detail(DetailView):
    model = Blog


""" class Coffeshop_create(CreateView):
    model = Coffeeshop
    fields = ["name", "address", "smoking", "description",
              "image1", "image2", "image3", "votes"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
 """

""" class Post_detail(DetailView):
    model = User_Post """


""" class All_blogs(ListView):
    model = Blog
    context_object_name = "blogs"
    ordering = ["-date"]
 """
