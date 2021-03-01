from django.test import TestCase


class TestSmokeTest(TestCase):
    def test_uno_mas_uno_igual_a_dos(self):
        self.assertEqual(1+1, 2)

    def test_true_es_true(self):
        self.assertTrue(True)
