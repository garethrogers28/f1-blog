from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm, CustomUserCreationForm
from .models import Comment, Post


def home(request):
    """
    Display paginated list of blog posts on the home page (6 per page).
    """
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, slug):
    """
    Display a single blog post with comments and like status.
    Handles comment submission for authenticated users.
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    liked = (
        post.likes.filter(id=request.user.id).exists()
        if request.user.is_authenticated
        else False
    )
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment posted successfully.')
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post': post, 'comments': comments, 'form': form,
        'liked': liked, 'like_count': post.likes.count(),
    })


@login_required
def edit_comment(request, pk):
    """
    Allow the comment author to edit their own comment.
    Only accessible to the comment's author.
    """
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        return redirect('post_detail', slug=comment.post.slug) #fix 
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully.')
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {
        'form': form, 'comment': comment,
    })


@login_required
def delete_comment(request, pk):
    """
    Allow the comment author to delete their own comment.
    Only accessible to the comment's author.
    """
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        return redirect('post_detail', slug=comment.post.slug)
    if request.method == 'POST':
        slug = comment.post.slug
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('post_detail', slug=slug)
    return render(request, 'blog/delete_comment.html', {'comment': comment})


@login_required
def like_post(request, slug):
    """
    Toggle like/unlike for a post by the logged-in user.
    Redirects back to the post detail page.
    """
    post = get_object_or_404(Post, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        messages.success(request, 'You unliked this post.')
    else:
        post.likes.add(request.user)
        messages.success(request, 'You liked this post!')
    return redirect('post_detail', slug=slug)


def register(request):
    """
    Handle user registration using a custom user creation form.
    On success, redirects to login page.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Account created successfully. You can now log in.',
            )
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
