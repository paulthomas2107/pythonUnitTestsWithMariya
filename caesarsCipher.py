import unittest
import string


def encrypt(message):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join([abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in enumerate(message)])
    return encrypted_message


class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.myMessage = 'paulThomas_1966 bread cheese, 8888 !!!'

    # Tests go here
    def test_inputExists(self):
        self.assertIsNotNone(self.myMessage)

    def test_inputType(self):
        self.assertIsInstance(self.myMessage, str)

    def test_funcReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.myMessage))

    def test_lenIO(self):
        self.assertEqual(len(self.myMessage), len(encrypt(self.myMessage)))

    def test_differentIO(self):
        self.assertNotIn(self.myMessage, encrypt(self.myMessage))

    def test_outputType(self):
        self.assertIsInstance(encrypt(self.myMessage), str)

    def test_shiftedCypher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join([abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0]
                                     for idx, char in enumerate(self.myMessage)])
        print(encrypted_message)
        self.assertEqual(encrypted_message, encrypt(self.myMessage))


if __name__ == '__main__':
    unittest.main()
