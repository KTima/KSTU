from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView,UpdateView,DeleteView,DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
# Create your views here.


def Homepage(request):
    news = News.objects.order_by("-tittle")[:6]
    programms = Programms.objects.order_by("date")[:3]
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request,"main/index.html",{"news":news,"programms":programms,"mapbox_access_token":mapbox_access_token})


class ProgrammsListView(LoginRequiredMixin,ListView):
    model = Programms
    template_name = 'main/programmslist.html'
    context_object_name = 'programmslist'
    raise_exception = True


class NewsListView(LoginRequiredMixin,ListView):
    model = News
    template_name = 'main/newslist.html'
    context_object_name = 'newslist'
    raise_exception = True

def Profile(request):
    if request.user.is_authenticated:
        return render(request,"main/cabinet.html")
    else:
        return HttpResponseForbidden()

def CreateProgramms(request):
    error = ''
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProgrammsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('programmslist')
            else:
                error = "Форма была неверно введена"
        form = ProgrammsForm
        context = {'form':form,
        'error':error,
        }
        return render(request,'main/createprogramms.html',context)
    else:
        return HttpResponseForbidden()

class ProgrammsUpdateView(LoginRequiredMixin,UpdateView):
    model = Programms
    template_name = 'main/createprogramms.html'
    form_class = ProgrammsForm
    success_url = reverse_lazy("programmslist")

class ProgrammsDeleteView(LoginRequiredMixin,DeleteView):
    model = Programms
    template_name = 'main/programmslist.html'
    success_url = reverse_lazy("programmslist")

def CreateNews(request):
    error = ''
    if request.user.is_authenticated:
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
    else:
        return HttpResponseForbidden()

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


class NewsDetailView(DetailView):
    model = News
    template_name = 'main/detailnews.html'
    context_object_name = 'news'


def CreateCons(request):
    error = ''
    if request.method == 'POST':
        form = ConsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            error = "Форма была неверно введена"
    form = ConsForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'main/consulting.html',context)

class ConsListView(LoginRequiredMixin,ListView):
    model = Consulting
    template_name = 'main/consultingview.html'
    context_object_name = 'conslist'
    raise_exception = True


