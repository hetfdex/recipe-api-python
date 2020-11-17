from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_super_user_valid_email(self):
        """
        Creates a super user from a valid email
        """
        email = 'test@test.com'
        password = 'Abcde12345!'
        user = get_user_model().objects.create_super_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_valid_email(self):
        """
        Creates a user from a valid email
        """
        email = 'test@test.com'
        password = 'Abcde12345!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_normalized_email(self):
        """
        Normalizes the email string
        """
        email = 'test@TEST.COM'
        password = 'Abcde12345!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email.lower())

    def test_create_user_null_email(self):
        """
        Does not create a user from a null email
        """
        password = 'Abcde12345!'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                password=password,
            )

    def test_create_user_empty_email(self):
        """
        Does not create a user from an empty email
        """
        password = 'Abcde12345!'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                '',
                password=password,
            )
