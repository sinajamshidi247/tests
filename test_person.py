import unittest
from person import Person

class PersonTest(unittest.TestCase):

    def setUp(self): #run before per test 
        self.p1  = Person("sina","jamshidi")
        self.p2 = Person("surush","jamshidi")

    def tearDown(self): # run after per test
        print("Done")

    def test_fullname(self):
        # p1 = Person("sina","jamshidi")
        # p2 = Person("surush","jamshidi")

        self.assertEqual(self.p1.fullname(),"sina jamshidi")
        self.assertEqual(self.p2.fullname(),"surush jamshidi")

    def test_email(self):

        # p1 = Person("sina","jamshidi")
        # p2 = Person("surush","jamshidi")


        self.assertEqual(self.p1.email(),"sinajamshidi@gmail.com")
        self.assertEqual(self.p2.email(),"surushjamshidi@gmail.com")

if __name__ == "__main__":
    unittest.main()