import lab1
import unittest


class T0_TestingQueue(unittest.TestCase):
    
    def test_basic_enqueue(self):
        #testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        
        self.assertEqual(q.printQueue(), [1,2,3,4])
        print("\n")

    def test_isEmpty(self):
        #testing the isEmpty operation
        print("\n")
        q = lab1.Queue()
        self.assertEqual(q.isEmpty(), True)
        q.enqueue(1)
        self.assertEqual(q.isEmpty(), False)
        print("\n")
    
    def test_enqueue_dequeue_enqueue(self):
        #testing funcionality if Queue is enqueued, then EMPTIED. Then also enqueued once more.
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.printQueue(), [])
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.printQueue(), [1,2])
        print("\n")

class T1_TestingStack(unittest.TestCase):
    
    def test_is_empty_false(self):
        #testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")

    def test_isEmpty(self):
        #testing the isEmpty operation
        print("\n")
        s = lab1.Stack()
        self.assertEqual(s.isEmpty(), True)
        s.push(1)
        self.assertEqual(s.isEmpty(), False)
        print("\n")

    def test_push_pop_push(self):
        #testing funcionality if Stack is pushed, then EMPTIED. Then also pushed once more.
        print("\n")
        s = lab1.Stack()
        s.push(1)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.printStack(), [])
        s.push(1)
        s.push(2)
        self.assertEqual(s.printStack(), [2,1])
        print("\n")

class T2_TestingPalindrome(unittest.TestCase):
    
    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ",string )
        self.assertEqual(p, False)
        print("\n")

    def test_capitals_string(self):
        # testing with capital string
        print("\n")
        string = "R  a    Ce        c      A r "
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ",string )
        self.assertEqual(p, True)
        print("\n")

if __name__ == '__main__':
    unittest.main()
