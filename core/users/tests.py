from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

    def test_new_superuser(self):
        User = get_user_model()
        super_user = User.objects.create_superuser(
            'testuser@super.com', 'username', 'first_name', 'password')
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'first_name')
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        self.assertEqual(str(super_user), "username")

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                User.objects.create_superuser(email='testuser@test.com', user_name='username', first_name='first_name',
                                              password='password', is_superuser=False)
            )

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                User.objects.create_superuser(email='testuser@test.com', user_name='username', first_name='first_name',
                                              password='password', is_staff=False)
            )

    def test_new_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            'testuser@user.com', 'username', 'first_name', 'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertEqual(user.user_name, 'username')
        self.assertEqual(user.first_name, 'first_name')
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)
        self.assertEqual(user.is_active, False)

        with self.assertRaises(ValueError):
            User.objects.create_user(email='', user_name='username', first_name='first_name', password='password')

