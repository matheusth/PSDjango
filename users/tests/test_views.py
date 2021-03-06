from django.test import TestCase
from users.models import CustomUser


class TestUserViews(TestCase):
    def test_unloged_user_should_see_the_home_page(self):
        """
            Tests if it is possible to view the homepage
        """
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

    def test_registered_user_should_be_able_to_authenticate(self):
        """
        Tests if a registred user is able to authenticate with success on the auth view
        """
        email = 'test_auth@teste.com'
        password = 'teste1234#'
        CustomUser.objects.create_user(fullname='Python 3', email=email, password=password)
        response = self.client.post('/auth', {
            'email': email,
            'password': password
        })
        self.assertRedirects(response, '/dashboard')
        self.assertIn('_auth_user_id', self.client.session)