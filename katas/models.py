from django.db import models
from user.models import Profile
import uuid


# Create your models here.
class Exercise(models.Model):
    Csharp = 'C#'
    Cplus = 'C++'
    Go = 'Go'
    Java = 'Java'
    JavaScript = 'JavaScript'
    PHP = 'PHP'
    Python = 'Python'
    Ruby = 'Ruby'
    Rust = 'Rust'
    Scala = 'Scala'
    SQL = 'SQL'
    TypeScript = 'TypeScript'

    language = [
        (Csharp, 'C#'),
        (Cplus, 'C++'),
        (Go, 'Go'),
        (Java, 'Java'),
        (JavaScript, 'JavaScript'),
        (PHP, 'PHP'),
        (Python, 'Python'),
        (Ruby, 'Ruby'),
        (Rust, 'Rust'),
        (Scala, 'Scala'),
        (SQL, 'SQL'),
        (TypeScript, 'TypeScript')
    ]

    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    cwID = models.CharField(max_length=200)
    description = models.TextField(max_length=300, blank=True, null=True)
    language = models.CharField(max_length=100, choices=language, default=JavaScript)
    tags = models.ManyToManyField('Tag', bland=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Tag(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name