import unittest

from tb_api.router import PathRouter


class TestRouterTestCase(unittest.TestCase):
    def test_01(self):
        router = PathRouter()
        router.add_path('get', '/clients/{client_id:int}', 'p1')
        router.add_path('get', '/clients/{client_id:int}/messages', 'p2')

        actual = router.search('get', '/clients/123')
        self.assertTrue(actual.match)
        self.assertEqual('p1', actual.data)
        self.assertEqual({'client_id': 123}, actual.params)

        actual = router.search('get', '/clients/123/messages')
        self.assertTrue(actual.match)
        self.assertEqual('p2', actual.data)
        self.assertEqual({'client_id': 123}, actual.params)


if __name__ == '__main__':
    unittest.main()
