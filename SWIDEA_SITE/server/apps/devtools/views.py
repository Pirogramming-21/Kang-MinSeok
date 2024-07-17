from django.shortcuts import render,redirect
from .models import DevTool
from .forms import DevToolForm
# Create your views here.

def dev_list(request):
    devtools = DevTool.objects.all()
    context = {
        "devtools":devtools
    }
    return render(request, "devtools/list.html", context)


def dev_create(request):
    print("ㅎㅇ")
    if request.method == "GET":
        form = DevToolForm()
        context = {"form":form}
        return render(request, "devtools/create.html", context)
    form = DevToolForm(request.POST)
    print(form)
    if form.is_valid():
        form.save()
    return redirect("devtools:manage")

def detail(request, pk):
    devtool = DevTool.objects.get(id=pk)
    related_ideas = devtool.idea.all()
    if not(related_ideas):
        related_ideas = []
    context = {
        "devtool":devtool,
        "related_ideas":related_ideas
    }
    return render(request, "devtools/detail.html", context)

def edit(request, pk):
    devtool = DevTool.objects.get(id=pk)
    if request.method == "GET":
        form = DevToolForm(instance=devtool)
        context = {"form":form, "pk":pk}
        return render(request,"devtools/edit.html", context)
    form = DevToolForm(request.POST, request.FILES, instance=devtool)
    if form.is_valid():
        form.save()
    return redirect("devtools:detail")

def delete(request, pk):
    DevTool.objects.get(id=pk).delete()
    return redirect("devtools:manage")