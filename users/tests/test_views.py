from django.test import TestCase


class TestUserViews(TestCase):
    def test_unloged_user_should_see_the_home_page(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')
