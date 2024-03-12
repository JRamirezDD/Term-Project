import unittest
from unittest.mock import patch
from CLIENT_RegistrationClient import RegistrationClient
from CLIENT_Client_Info import Client_Info

class TestRegistrationClient(unittest.TestCase):
    def setUp(self):
        # Define common setup steps here
        self.server_host = '127.0.0.1'
        self.server_port = 9999
        self.client_nickname = "Omar"
        self.client_private_ip = "10.16.140.176"
        self.client_listening_port = 50315
        self.client_info = Client_Info(self.client_nickname, self.client_private_ip, self.client_listening_port)
        self.client = RegistrationClient(self.server_host, self.server_port, self.client_info)

    def tearDown(self):
        # Define cleanup steps here
        pass

    def test_register_with_server(self):
        # Test registering with the server
        with patch('builtins.socket.socket') as mock_socket:
            mock_socket.return_value.recv.return_value = b'success'
            response = self.client.register_with_server(self.client_info)
            self.assertEqual(response, 'success')

    # Define more test methods for other functionalities

if __name__ == '__main__':
    unittest.main()
