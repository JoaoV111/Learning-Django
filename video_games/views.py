from django.shortcuts import render, get_object_or_404
from .models import Console

def index(request):
    console_list = Console.objects.order_by('id')[:5]
    context = {'console_list': console_list}
    return render(request, 'video_games/index.html', context)


def detail(request, console_id):
    console = get_object_or_404(Console, pk=console_id)
    comment_list = console.comments_set.order_by('-pub_date')[:5]
    return render(request, 'video_games/detail.html', {'console': console, 'comment_list': comment_list})
