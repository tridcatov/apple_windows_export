from unittest import TestCase
from DateResolver import DateResolver

class TestDateResolver(TestCase):
    def test_resolve(self):
        resolver = DateResolver()
        self.assertEqual((1, 1, 1970), resolver.resolve("01 января 1970 г."))
        self.assertEqual((1, 1, 1970), resolver.resolve("Непонятное место, 01 января 1970 г."))
        self.assertEqual((12, 12, 2012), resolver.resolve("Встреча миллениума на Кропоткинской, 12 декабря 2012 г."))
