import unittest
import os
import tempfile
import ccwc as c

class CCWCTestCase(unittest.TestCase):

    def setUp(self):
        """Create a temporary test file before each test"""
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
        self.test_file.write("Hello world\nThis is a test file.\n12345\n")
        self.test_file.close()  # Close it so the functions can read from it

    def tearDown(self):
        """Remove the temporary test file after each test"""
        os.remove(self.test_file.name)

    def test_file_name_return(self):
        self.assertEqual(os.path.basename(self.test_file.name), c.file_name(self.test_file.name))

    def test_get_bytes(self):
        expected_bytes = os.path.getsize(self.test_file.name)
        self.assertEqual(expected_bytes, c.get_bytes(self.test_file.name))

    def test_get_lines(self):
        expected_lines = ["Hello world\n", "This is a test file.\n", "12345\n"]
        self.assertEqual(expected_lines, c.get_lines(self.test_file.name))

    def test_count_lines(self):
        self.assertEqual(3, c.count_lines(self.test_file.name))

    def test_count_word(self):
        self.assertEqual(8, c.count_word(self.test_file.name))  # ["Hello", "world", "This", "is", "a", "test", "file.", "12345"]

    def test_count_char(self):
        line_array = c.get_lines(self.test_file.name)
        expected_chars = sum(len(line) for line in line_array)
        self.assertEqual(expected_chars + len(line_array),
                         c.count_char(self.test_file.name))

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            c.get_bytes("non_existent_file.txt")

    def test_empty_file(self):
        """Test behavior on an empty file"""
        empty_file = tempfile.NamedTemporaryFile(delete=False)
        empty_file.close()
        self.assertEqual(0, c.get_bytes(empty_file.name))
        self.assertEqual(0, c.count_lines(empty_file.name))
        self.assertEqual(0, c.count_word(empty_file.name))
        self.assertEqual(0, c.count_char(empty_file.name))
        os.remove(empty_file.name)

if __name__ == '__main__':
    unittest.main()
