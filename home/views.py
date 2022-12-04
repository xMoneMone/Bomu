from django.shortcuts import render
from posts.models import CanvasPost
from django.db.models import Count
from django.views import View


class Home(View):

    def get(self, request):
        tag = "popular"
        posts = CanvasPost.objects.filter().annotate(num=Count('canvaslike')).order_by('-num')
        context = {'posts': posts,
                   'tag': tag}
        return render(request, template_name="home.html", context=context)


class HomeNew(View):

    def get(self, request):
        tag = "new"
        posts = CanvasPost.objects.all().order_by('-id')
        context = {'posts': posts,
                   'tag': tag}
        return render(request, template_name="home.html", context=context)
