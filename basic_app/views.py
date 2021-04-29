# from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, UpdateView, DeleteView
from . import models
# from django.http import HttpResponse


# def index(req):
#     return render(req, 'index.html')


# class CBView(View):
#     def get(self, request):
#         return HttpResponse("class based view")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic injection'
        return context


class SchoolListView(ListView):
    # define you own name
    context_object_name = 'schools'
    model = models.School  # defined by default without context_object_name: school_list
    # school_list


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School  # school by default (without context_object_name)
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(UpdateView):
    fields = ('name', 'principal', 'location')
    model = models.School
    template_name = 'basic_app/school_form.html'


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    # connect model
    model = models.School
    template_name = 'basic_app/school_conform_delete.html'
    # go back to school list after delete
    success_url = reverse_lazy("basic_app:list")
