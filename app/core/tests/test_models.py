from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class UserTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Teste creating a new user iwth an email is successful"""
        email = "test@test.com"
        password = "testpass123"
        user = User.objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'teste@TESTE.com'
        user = User.objects.create_user(email, 'testpass123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Teste creating user with no email raises error"""
        with self.assertRaises(ValueError):
            User.objects.create_user(None, 'testpass123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = User.objects.create_superuser(
            'teste@teste.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
