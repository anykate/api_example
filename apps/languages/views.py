from django.shortcuts import render, get_object_or_404
from .models import Language, State


def index(request):
    return render(request, 'languages/index.html', {})


def language_detail(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    return render(request, 'languages/language-detail.html', {'language': language})


def state_detail(request, state_id):
    state = get_object_or_404(State, id=state_id)
    return render(request, 'languages/state-detail.html', {'state': state})
