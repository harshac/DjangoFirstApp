from django.test import TestCase, Client

class MySiteTest(TestCase):
    def setUp(self):
        self.client_stub = Client()

    def test_index_route(self):
        response = self.client_stub.get('/myapp/')
        self.assertEquals(response.status_code,200)

    def test_content(self):
        response = self.client_stub.get('/myapp/')
        self.assertTrue(response.content.__contains__("Hello"))

    def test_welcome_route(self):
        response = self.client_stub.get('/myapp/django/')
        self.assertEquals(response.status_code,200)

    def test_welcome_content(self):
        response = self.client_stub.get('/myapp/django/')
        self.assertTrue(response.content.__contains__("django"))
        self.assertTrue(response.content.__contains__("Welcome"))

    def test_create_user_route(self):
        response = self.client_stub.get('/myapp/new_user/')
        self.assertEquals(response.status_code, 200)

