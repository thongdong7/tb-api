import unittest

from tb_api.router import PathNodeRouter


class TestRouterTestCase(unittest.TestCase):
    def test_01(self):
        router = PathNodeRouter()
        router.add_path('get', '/clients/{client_id}', 'p1')
        router.add_path('get', '/clients/{client_id}/messages', 'p2')

        actual = router.search('get', '/clients/123')
        self.assertEqual('p1', actual.data)
        self.assertEqual({'client_id': '123'}, actual.params)

        actual = router.search('get', '/clients/123/messages')
        self.assertEqual('p2', actual.data)
        self.assertEqual({'client_id': '123'}, actual.params)


if __name__ == '__main__':
    unittest.main()
