from django.shortcuts import render
from app.models import Post
from app.forms import CommentForm

# Create your views here.
def index(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'app/index.html',context)

def post_page(request,slug):
    post=Post.objects.get(slug=slug)
    form=CommentForm()

    if request.POST:
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid:
            comment=comment_form.save(commit=False)
            postid=request.POST.get['post_id']
            post=Post.objects.get(id=postid)
            comment.post=post
            comment.save()


    if post.view_count is None:
        post.view_count=1
    else:
        post.view_count=post.view_count+1
    post.save()
    context={'post':post,'form':form}
    return render(request,'app/post.html',context)