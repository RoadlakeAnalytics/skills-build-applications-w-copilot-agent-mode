from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        app_label = 'tracker'

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

    class Meta:
        app_label = 'tracker'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    class Meta:
        app_label = 'tracker'

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()

    class Meta:
        app_label = 'tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes

    class Meta:
        app_label = 'tracker'
