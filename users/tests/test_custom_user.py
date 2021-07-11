from django.test import TestCase
from users.models import CustomUser


class TestCustomUser(TestCase):

    def setUp(self) -> None:
        self.fullname = 'Elixir Golang'

    def test_create_user_should_throw_error_if_no_email_is_provided(self):
        """
        Tests if the create_user method throws an error, in case the email is not provided.
        """
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(fullname=self.fullname, email='', password='teste564#')

    def test_create_user_should_throw_error_if_no_password_is_provided(self):
        """
        Tests if the create_user method throws an error in case no password is provided
        """
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(fullname=self.fullname, email='teste@teste.com', password='')

    def test_create_user_should_create_a_user_if_provided_all_information(self):
        """
        Tests if the create user method works in case the fullname, the email and the password are provided
        """
        user = CustomUser.objects.create_user(fullname=self.fullname, email='teste@teste.com', password='teste564#')

        self.assertEqual(user.fullname, self.fullname.upper())
