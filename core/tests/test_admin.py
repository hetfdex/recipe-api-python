from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminTest(TestCase):
    def setUp(self):
        admin_email = 'admin@test.com'
        admin_password = 'Abcde12345?'
        email = 'test@test.com'
        password = 'Abcde12345!'
        name = 'name'

        self.client = Client()

        self.admin_user = get_user_model().objects.create_superuser(
            email=admin_email,
            password=admin_password,
        )

        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name=name,
        )

    def test_user_list(self):
        """User list page renders correctly"""
        url = reverse('admin:core_user_changelist')

        response = self.client.get(url)

        self.assertContains(response, self.user.email)
        self.assertContains(response, self.user.name)

    def test_user_edit(self):
        """User edit page renders correctly"""
        url = reverse('admin:core_user_change', args=[self.user.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_user_add(self):
        """User add page renders correctly"""
        url = reverse('admin:core_user_add')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
