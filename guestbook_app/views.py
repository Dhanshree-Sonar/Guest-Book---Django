# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Comment
from .forms import CommentForm

def index(request):
    comments = Comment.objects.order_by('-date_added')
    context = {'comments': comments}

    return render(request, 'guestbook_app/index.html', context)

def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'],
                comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')
    else:
        form = CommentForm()

    context = {'form': form}
    return render(request, 'guestbook_app/sign.html', context)
