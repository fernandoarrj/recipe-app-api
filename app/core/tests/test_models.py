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
