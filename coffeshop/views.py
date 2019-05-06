from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Coffeeshop
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import F


class All_coffeeshops(ListView):
    model = Coffeeshop
    context_object_name = "coffeeshops"

    ordering = ["-date"]
    paginate_by = 3

    def get_queryset(self):

        try:
            name = self.request.GET.get('name')
        except:
            name = ""
        if name:
            objects_list = Coffeeshop.objects.filter(name__icontains=name)
        else:
            objects_list = Coffeeshop.objects.all()
        return objects_list


class All_user_coffeeshops(ListView):
    model = Coffeeshop
    context_object_name = "coffeeshops"
    template_name = "coffeshop/user_coffeeshops.html"
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("user"))
        return Coffeeshop.objects.filter(user=user).order_by('-date')


class Coffeshop_detail(DetailView):
    model = Coffeeshop


class Coffeshop_create(LoginRequiredMixin, CreateView):
    model = Coffeeshop
    readonly_fields = ("date")
    fields = ["name", "address", "smoking", "working_hours_weekdays", "working_hours_saturday", "working_hours_sunday", "image1", "description",
              "image2", "description2", "image3",  "description3"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Coffeshop_update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Coffeeshop
    fields = ["name", "address", "smoking", "working_hours_weekdays", "working_hours_saturday", "working_hours_sunday", "image1", "description",
              "image2", "description2", "image3", "description3"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coffeeshop = self.get_object()
        if self.request.user == coffeeshop.user:
            return True
        return False


class Coffeshop_delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Coffeeshop
    success_url = "/"

    def test_func(self):
        coffeeshop = self.get_object()
        if self.request.user == coffeeshop.user:
            return True
        return False


class CF(F):
    ADD = '||'


@login_required
def upvote(request, pk, username):

    if request.method == "POST":
        coffeeshop = get_object_or_404(Coffeeshop, pk=pk)

        print("mica" + coffeeshop.voted)
        if username in coffeeshop.voted:
            return redirect("/coffeeshops" + "/" + str(coffeeshop.id))
        else:
            if username not in coffeeshop.voted:
                Coffeeshop.objects.filter(pk=pk).update(
                    voted=CF("voted") + username)

            coffeeshop = get_object_or_404(Coffeeshop, pk=pk)
            coffeeshop.votes += 1
            coffeeshop.save()
            return redirect("/coffeeshops" + "/" + str(coffeeshop.id))
