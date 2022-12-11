from django.test import TestCase


class CanvasTestCase(TestCase):
    def test_canvas(self):
        response = self.client.get('canvas')
        self.assertEqual(response, 200)

