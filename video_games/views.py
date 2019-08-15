from django.shortcuts import render, get_object_or_404
from .models import Console
from .forms import CommentsForm
from django.utils import timezone

def index(request):
    console_list = Console.objects.order_by('id')[:5]
    context = {'console_list': console_list}
    return render(request, 'video_games/index.html', context)


def detail(request, console_id):
	console = get_object_or_404(Console, pk=console_id)
	comment_list = console.comments_set.order_by('-pub_date')[:5]
	console_list = Console.objects.order_by('id')[:5]
	return render(request, 'video_games/detail.html', {'console': console, 'comment_list': comment_list,
													   'console_list': console_list})

def comment_detail(request, console_id):
	if request.method == 'POST':
		form = CommentsForm(request.POST)
		if form.is_valid():
			console = Console.objects.get(pk=console_id)
			comment = form.cleaned_data['comment_txt']
			score = form.cleaned_data['score']
			console.comments_set.create(comment_txt=comment, score=score, pub_date=timezone.now())
			return render(request, 'video_games/submit.html', {'console_id': console_id})

	form = CommentsForm(request.POST)
	return render(request, 'video_games/comment.html', {'form': form})
