from .models import Exercise, Tag
from django.db.models import Q

def search_katas(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    profile = request.user.profile
    exercises = profile.exercise_set.all().distinct().filter(
        Q(name__icontains=search_query) | 
        Q(description__icontains=search_query) |
        Q(language__icontains=search_query) |
        Q(tags__in=tags)
    )

    return exercises, search_query