from django.shortcuts import render, redirect
from .models import Exercise, Tag
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ExerciseForm
from .utils import search_katas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse

# Create your views here.


def katas(request):
    return render(request, 'katas/katas.html')

@login_required(login_url="login")
def my_katas(request):
    exercises, search_query = search_katas(request)
    Csharp = exercises.filter(language='C#')
    Cplus = exercises.filter(language='C++')
    Go = exercises.filter(language='Go')
    Java = exercises.filter(language='Java')
    JavaScript = exercises.filter(language='JavaScript')
    php = exercises.filter(language='php')
    Python = exercises.filter(language='Python')
    Ruby = exercises.filter(language='Ruby')
    Rust = exercises.filter(language='Rust')
    Scala = exercises.filter(language='Scala')
    TypeScript = exercises.filter(language='TypeScript')
    
    context = {
        'C#': Csharp, 
        'C++': Cplus,
        'Go': Go,
        'Java': Java,
        'JavaScript': JavaScript,
        'php': php,
        'Python': Python,
        'Ruby': Ruby,
        'Rust': Rust,
        'Scala': Scala,
        'TypeScript': TypeScript
    }

    return render(request, 'katas/my_katas.html', context)


@login_required(login_url="login")
def kata(request, pk):
    exercise_obj = Exercise.objects.get(id=pk)
    tags = exercise_obj.tags.all()
    context = {'exercise': exercise_obj, 'tags': tags}
    return render(request, 'katas/single_kata.html', context)


@login_required(login_url="login")
def create_kata(request):
    profile = request.user.profile
    form = ExerciseForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.owner = profile
            exercise.save()
            messages.success(request, 'Kata successfully registered!')

            for tag in newtags:
                tag = Tag.objects.create(name=tag)
                tag.owner = profile
                tag.save()
                exercise.tags.add(tag)

            return redirect('katas')
    
    context = {'form': form}
    return render(request, 'katas/kata_form.html', context)


@login_required(login_url="login")
def update_kata(request, pk):
    page = 'update'
    profile = request.user.profile
    exercise = profile.exercise_set.get(id=pk)
    tags = exercise.tags.all()
    form = ExerciseForm(instance=exercise)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            exercise = form.save()
            messages.success(request, 'Kata updated!')
            for tag in newtags:
                tag = Tag.objects.create(name=tag)
                tag.owner = profile
                tag.save()
                exercise.tags.add(tag)
            return redirect('kata', pk=exercise.id)

    context = {'page': page, 'form': form, 'tags': tags, 'exercise': exercise}
    return render(request, 'katas/kata_form.html', context)


@login_required(login_url="login")
def delete_kata(request, pk):
    profile = request.user.profile
    exercise = profile.exercise_set.get(id=pk)

    if request.method == 'POST':
        exercise.delete()
        messages.success(request, 'Kata deleted!')
        return redirect('katas')
    
    context = {'object': exercise}
    return render(request, 'delete_template.html', context)


@login_required(login_url="login")
def delete_tag(request, pk):
    profile = request.user.profile
    tag = profile.tag_set.get(id=pk)

    if request.method == 'POST':
        tag.delete()
        messages.success(request, 'Tag deleted!')
        return redirect(request.GET['next'])
    
    context = {'object': tag}
    return render(request, 'delete_template.html', context)
