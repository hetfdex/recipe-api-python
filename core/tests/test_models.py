from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def setUp(self):

        self.email = 'test@test.com'
        self.emailUpper = 'test@TEST.COM'
        self.password = 'Abcde12345!'

    def test_create_superuser_valid_email(self):
        """
        Creates a superuser from a valid email
        """
        user = get_user_model().objects.create_superuser(
            email=self.email,
            password=self.password,
        )

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_superuser_normalized_email(self):
        """
        Normalizes the email of the superuser
        """
        user = get_user_model().objects.create_superuser(
            email=self.emailUpper,
            password=self.password,
        )

        self.assertEqual(user.email, self.emailUpper.lower())

    def test_create_superuser_null_email(self):
        """
        Does not create a superuser from a null email
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(
                None,
                password=self.password,
            )

    def test_create_superuser_empty_email(self):
        """
        Does not create a superuser from an empty email
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(
                '',
                password=self.password,
            )

    def test_create_user_valid_email(self):
        """
        Creates a user from a valid email
        """
        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password,
        )

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_create_user_normalized_email(self):
        """
        Normalizes the email of the user
        """
        user = get_user_model().objects.create_user(
            email=self.emailUpper,
            password=self.password,
        )

        self.assertEqual(user.email, self.emailUpper.lower())

    def test_create_user_null_email(self):
        """
        Does not create a user from a null email
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                password=self.password,
            )

    def test_create_user_empty_email(self):
        """
        Does not create a user from an empty email
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                '',
                password=self.password,
            )
