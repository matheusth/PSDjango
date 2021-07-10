from django.test import TestCase
from users.models import CustomUser


class TestUserViews(TestCase):
    def test_unloged_user_should_see_the_home_page(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

    def test_registered_user_should_be_able_to_authenticate(self):
        email = 'test_auth@teste.com'
        password = 'teste1234#'
        CustomUser.objects.create_user(fullname='Python 3', email='teste_auth@teste.com', password='teste1234#')
        response = self.client.post('/auth', {
            'email': email,
            'password': password
        })
        self.assertRedirects(response, '/dashboard')
