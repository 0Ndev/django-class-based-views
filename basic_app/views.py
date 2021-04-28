from django.shortcuts import render
from django.views.generic import View, TemplateView
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
