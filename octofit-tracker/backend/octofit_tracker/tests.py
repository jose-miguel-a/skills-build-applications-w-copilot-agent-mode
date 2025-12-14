from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)
        Activity.objects.create(user=tony, type='Run', duration=30, distance=5)
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Leaderboard.objects.create(user=tony, points=100)

    def test_user_team(self):
        tony = User.objects.get(email='tony@marvel.com')
        self.assertEqual(tony.team.name, 'Team Marvel')

    def test_leaderboard_points(self):
        tony = User.objects.get(email='tony@marvel.com')
        entry = Leaderboard.objects.get(user=tony)
        self.assertEqual(entry.points, 100)
