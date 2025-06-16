from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    """Test cases for Stack"""

    def setUp(self):
        """Setup before each test"""
        self.stack = Stack()

    def tearDown(self):
        """Tear down after each test"""
        self.stack = None

    def test_push(self):
        """Test pushing an item into the stack"""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(40)
        self.stack.push(15)
        self.stack.push(30)
        self.assertEqual(len(self.stack.items), 3)
        self.assertEqual(self.stack.peek(), 30)
        

    def test_pop(self):
        """Test popping an item of off the stack"""
        self.stack.push(5)
        self.stack.push(10)
        self.assertEqual(self.stack.pop(), 10)
        self.assertEqual(len(self.stack.items), 1)

    def test_peek(self):
        """Test peeking at the top the stack"""
        self.stack.push(3)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)

        

    def test_is_empty(self):
        """Test if the stack is empty"""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())   
