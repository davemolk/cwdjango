from django.forms import ModelForm
from .models import Exercise

class ExerciseForm(ModelForm):
    class Meta:
        model: Exercise
        fields = ['name', 'description', 'language']
        labels = {
            'name': 'Name of Kata',
            'description': 'Description of Kata'
        }

    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})