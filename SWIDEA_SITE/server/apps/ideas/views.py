from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm
# Create your views here.

def main(request):
    ideas = Idea.objects.all()
    sort = request.GET.get('sort')
    if sort == '관심도순':
        ideas = Idea.objects.all().order_by('interest')
    elif sort == '등록순':
        ideas = Idea.objects.all().order_by('id')
    elif sort == '최신순':
        ideas = Idea.objects.all().order_by('-id')
    context = {
        "ideas":ideas
    }
    return render(request, "ideas/main.html", context)

def create(request):
    print("ㅎㅇ")
    if request.method == "GET":
        form = IdeaForm()
        context = {"form":form}
        return render(request, "ideas/create.html", context)
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect("ideas:main")

def detail(request, pk):
    idea = Idea.objects.get(id=pk)
    devtool = idea.devtool
    context = {
        "idea":idea,
        "devtool":devtool
    }
    return render(request, "ideas/detail.html", context)

def edit(request, pk):
    idea = Idea.objects.get(id=pk)
    if request.method == "GET":
        form = IdeaForm(instance=idea)
        context = {"form":form, "pk":pk}
        return render(request,"ideas/edit.html", context)
    form = IdeaForm(request.POST, request.FILES, instance=idea)
    if form.is_valid():
        form.save()
    return redirect("ideas:detail")

def delete(request, pk):
    Idea.objects.get(id=pk).delete()
    return redirect("ideas:main")