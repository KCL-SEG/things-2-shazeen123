from .models import Thing
from django.core.exceptions import ValidationError
from django.test import TestCase

class ThingModelTestCase(TestCase):

    def setUp(self):
        self.thing = Thing.objects.create_user(
            name='@john', 
            description='Hi I am John.',
            quantity =10
        )

    def test_assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('User should be valid')

    def test_assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()