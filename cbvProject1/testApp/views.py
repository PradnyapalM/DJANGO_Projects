from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.

class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1> This is a Class Based Views </h1>')
    
class HelloWorldTemplateView(TemplateView):
    template_name = 'testApp/result.html'

class HelloWorldContext(TemplateView):
    template_name = 'testApp/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Name'] = 'Tips'
        context['Subject'] = 'Python'
        context['Marks'] = 100
        return context
