from django.test import TestCase
from django.urls import reverse
from .models import User, Queue, Ticket

class CoreViewsTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

class CoreModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.queue = Queue.objects.create(name='Test Queue', email_address='queue@example.com')

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.username, 'testuser')

    def test_queue_creation(self):
        self.assertEqual(Queue.objects.count(), 1)
        self.assertEqual(self.queue.name, 'Test Queue')

    def test_ticket_creation(self):
        ticket = Ticket.objects.create(
            title='Test Ticket',
            description='This is a test ticket.',
            queue=self.queue,
            submitter_email='submitter@example.com'
        )
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(ticket.title, 'Test Ticket')
        self.assertEqual(ticket.queue, self.queue)
