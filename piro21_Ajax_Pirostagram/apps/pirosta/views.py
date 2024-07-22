from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import User, Post, Comment
from apps.pirosta.forms import SignupForm
# Create your views here.

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect("pirosta:posts")
        else:
            return render(request, "login.html", {"form": form})
    else:
        form = AuthenticationForm()  # 장고에서 지원하는 로그인 폼?
        return render(request, "login.html", {"form": form})
    
def signup(request):  # 회원가입
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # auth.login(request, user)
            return redirect("pirosta:login")
        else:
            return render(request, "signup.html", {"form": form})
    else:  # get메소드
        form = SignupForm()  # 회원가입 폼 전달
        return render(request, "signup.html", {"form": form})

def logout(request):
    auth.logout(request)
    return redirect("pirosta:login")

def posts(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        comments = Comment.objects.all()
        context = {
            "posts": posts,
            "comments": comments
        }
        return render(request, "posts.html", context)
    else:
        return redirect("pirosta:login")

def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
                Post.objects.create(
                    writer = request.user,
                    content = request.POST["content"],
                    photo = request.FILES["photo"]
                )
                return redirect('pirosta:posts')
        elif request.method == 'GET':
            return render(request, 'create_post.html')
    else:
        return redirect("pirosta:login")
    
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Post, Comment

@csrf_exempt
def like_ajax(request):
    data = json.loads(request.body)
    post_id = data['id']
    is_checked = data['is_checked']

    post = Post.objects.get(id=post_id)
    user = request.user

    if is_checked:
        post.likedUser.add(user)
    else:
        post.likedUser.remove(user)

    liked_count = post.likedUser.count()
    return JsonResponse({'liked': liked_count, 'is_checked': is_checked})

@csrf_exempt
def comment_ajax(request):
    data = json.loads(request.body)
    post_id = data['id']
    content = data.get('content', None)

    if content:
        post = Post.objects.get(id=post_id)
        user = request.user
        comment = Comment.objects.create(writer=user, postInfo=post, content=content)

        return JsonResponse({
            'comment': comment.content,
            'writer': comment.writer.username,
            'id': comment.id
        })

    else:
        comments = Comment.objects.filter(postInfo=post_id).values('id', 'writer__username', 'content','writer_id')
        return JsonResponse(list(comments), safe=False)
    
def delete_comment_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)
        comment_id = data['comment_id']
        comment = Comment.objects.get(id=comment_id)
        
        if request.user == comment.writer:
            comment.delete()
            return JsonResponse({'status': 'success'})
        
        return JsonResponse({'status': 'error', 'message': 'Permission denied'}, status=403)