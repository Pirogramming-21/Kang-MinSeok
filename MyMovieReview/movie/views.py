from django.shortcuts import render, redirect
from .models import Review
# Create your views here.

def movie_list(request):
    reviews = Review.objects.all()
    context = {
        "reviews" : reviews
    }
    print(reviews)
    return render(request, 'review_list.html', context)

def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        "review" : review
    }
    return render(request, "review_detail.html", context)

def review_create(request): 
    if request.method == "POST":
        Review.objects.create(
            title = request.POST["title"],
            director = request.POST["director"],
            actor = request.POST["actor"],
            year = request.POST["year"],
            genre = request.POST["genre"],
            rate = request.POST["rate"],
            running_time = request.POST["running_time"],
            content = request.POST["content"]
        )
        reviews = Review.objects.all()
        print(reviews)
        return redirect("/movie")
    else:    
        genres = Review.movie_genre
        print(f"장르는 = {genres}")
        context = {
            'genres' : genres
        }
    return render(request, "review_create.html", context)

def review_edit(request, pk):
    review = Review.objects.get(id=pk)
    genres = Review.movie_genre
    if request.method == "POST":
        review.title = request.POST["title"]
        review.director = request.POST["director"]
        review.actor = request.POST["actor"]
        review.year = request.POST["year"]
        review.genre = request.POST["genre"]
        review.rate = request.POST["rate"]
        review.running_time = request.POST["running_time"]
        review.content = request.POST["content"]

        review.save()

        return redirect(f"/movie/{pk}")
    context = {
        "review" : review,
        'genres' : genres
    }
    return render(request, "review_edit.html", context)

def review_delete(request, pk):
    if request.method == "POST":
        review=Review.objects.get(id=pk)
        review.delete()
    return redirect("/movie")
