from django.test import TestCase


class Test(TestCase):
    def test_polls_list_access (self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class Quiz(TestCase):
    def test_create_poll (self):
        poll = Quiz.objects.create(
        title="Test POll 1",
        description="description"
 )
        self.assertEqual(poll.title, "Test POll 1")
        self.assertEqual(poll.description, "description")
        self.assertTrue(poll.is_active)
