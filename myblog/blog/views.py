from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug":"hike-in-the-mountain",
        "image":"mountains.jpg",
        "author":"dev jain",
        "date":date(2021,7,21),
        "title":"mountain hiking",
        "excerpt":"lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit",  
        "content":"""
    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit" 

    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit"
    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sitlorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit"
    """
    },
    {
        "slug":"hike-in-the-mountain",
        "image":"mountains.jpg",
        "author":"dev jain",
        "date":date(2021,9,21),
        "title":"mountain hiking",
        "excerpt":"lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit",  
        "content":"""
    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit" 

    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit"
    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sitlorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit"
    """
    },
    {
        "slug":"hike-in-the-mountain",
        "image":"mountains.jpg",
        "author":"dev jain",
        "date":date(2021,12,21),
        "title":"mountain hiking",
        "excerpt":"lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit",  
        "content":"""
    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit" 

    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit"
    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sitlorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit"
    """
    },
    {
        "slug":"hike-in-the-mountain",
        "image":"mountains.jpg",
        "author":"dev jain",
        "date":date(2021,4,21),
        "title":"mountain hiking",
        "excerpt":"lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit",  
        "content":"""
    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit" 

    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit"
    lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sitlorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit lorem ipsum dolor amit sit"
    """
    },
]

def get_date(post):
    return post['date']
# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{"posts":latest_posts})

def posts(request):
    return render(request,"blog/all-posts.html",{"all_posts":all_posts})

def post_detail(request,slug):
    identified_post = next(post for post in all_posts if post['slug']==slug)
    return render(request,"blog/post-detail.html",{"post":identified_post})
