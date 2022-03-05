from pyexpat import model
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def Homepage(request):
    news = News.objects.order_by("-tittle")[:10]
    return render(request,"main/index.html",{"news":news})

class NewsListView(LoginRequiredMixin,ListView):
    model = News
    template_name = 'main/newslist.html'
    context_object_name = 'newslist'
    raise_exception = True

def CreateNews(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('News')
        else:
            error = "Форма была неверно введена"
    form = NewsForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'main/createnews.html',context)

class NewsUpdateView(LoginRequiredMixin,UpdateView):
    model = News
    template_name = 'main/createnews.html'
    form_class = NewsForm
    success_url = reverse_lazy("News")

class NewsDeleteView(LoginRequiredMixin,DeleteView):
    model = News
    template_name = 'main/newslist.html'
    success_url = reverse_lazy("News")

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *,object_list=None,**kwargs):
        return super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('homepage')    

def logout_user(request):
    logout(request)
    return redirect('homepage')
