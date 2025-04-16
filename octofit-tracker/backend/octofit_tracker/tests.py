from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from bson import ObjectId

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            _id=ObjectId(),
            username='testuser',
            email='test@example.com',
            password='testpass'
        )
        self.team = Team.objects.create(
            _id=ObjectId(),
            name='Test Team'
        )
        self.activity = Activity.objects.create(
            _id=ObjectId(),
            user=self.user,
            activity_type='Running',
            duration=timedelta(minutes=30)
        )
        self.leaderboard = Leaderboard.objects.create(
            _id=ObjectId(),
            user=self.user,
            score=100
        )
        self.workout = Workout.objects.create(
            _id=ObjectId(),
            name='Test Workout',
            description='Test workout description'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, timedelta(minutes=30))

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 100)

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Test Workout')

class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            _id=ObjectId(),
            username='testuser',
            email='test@example.com',
            password='testpass'
        )

    def test_list_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_team(self):
        url = reverse('team-list')
        data = {
            'name': 'New Team',
            'members': []
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)

    def test_create_activity(self):
        url = reverse('activity-list')
        data = {
            'user': str(self.user._id),
            'activity_type': 'Running',
            'duration': '00:30:00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_leaderboard_entry(self):
        url = reverse('leaderboard-list')
        data = {
            'user': str(self.user._id),
            'score': 100
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_workout(self):
        url = reverse('workout-list')
        data = {
            'name': 'New Workout',
            'description': 'Workout description'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
