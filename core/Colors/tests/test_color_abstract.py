from django.test import TestCase
from ..models import ColorAbstract


class CategoryColorTestCase(TestCase):
    def test_to_hex_color(self):
        correct_values = [
            ('#ffffff', '#FFFFFF'),
            ('#FFFFFF', '#FFFFFF'),
            ('#123aaa', '#123AAA'),
            ('#123AAA', '#123AAA'),
        ]
        incorrect_values = [
            '#abcdeff',
            '#abcde',
            '#1234567',
            '#12345',
            '#abcdeq',
        ]
        correct_values.extend([(value.replace('#', ''), expected) for value, expected in correct_values])
        incorrect_values.extend([item.replace('#', '') for item in incorrect_values])

        for value, expected in correct_values:
            self.assertEqual(ColorAbstract.to_hex_color(value), expected)

        for value in incorrect_values:
            self.assertRaises(ValueError, ColorAbstract.to_hex_color, value=value)
