from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating user with email is successful"""
        email = 'testing@gmail.com'
        password = 'testingpwd123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'testing@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='testingpwd123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Creating user with no email address raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testingpwd123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
                'testing@gmail.com',
                'testingpwd123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
