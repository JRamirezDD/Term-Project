import unittest
from unittest.mock import patch
from CLIENT_RegistrationClient import RegistrationClient
from UTILS_networking import *
from CLIENT_Client_Info import Client_Info

class TestMyClient(unittest.TestCase):
    def setUp(self):
        # Set up necessary test fixtures
        self.client = RegistrationClient
        server_host = '127.0.0.1'
        server_port = 9999
        test_client_nickname = "TestClient"
        test_client_ip = get_private_ip()
        test_client_port = get_free_port()
        self.test_client_info = Client_Info(test_client_nickname,test_client_ip,test_client_port)
        self.test_client = RegistrationClient(server_host, server_port, self.test_client_info)


    def test_register_with_server(self):
        # Mock the response from the server
        mock_response = b'{"status": "success"}'

        # Patch the socket module to return the mock response
        with patch('socket.socket') as mock_socket:
            mock_socket_instance = mock_socket.return_value
            mock_socket_instance.recv.return_value = mock_response

            # Call the method under test
            response = self.test_client.register_with_server(self.test_client_info)

            # Verify the expected behavior
            self.assertEqual(response, 'success')

if __name__ == '__main__':
    unittest.main()
