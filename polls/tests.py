from django.test import TestCase


class BasicTestCase(TestCase):
    def test_addition(self):
        """Basic sanity check to ensure tests run."""
        print("Hello, World!")
        self.assertEqual(1 + 1, 2)

    def test_truth(self):
        """Ensure boolean logic works."""
        self.assertTrue(True)
