import unittest 
import one



class OneTest(unittest.TestCase):
    
    def test_zarb(self):
        self.assertEqual(one.zarb(2,3),6)
        self.assertEqual(one.zarb(0,3),0)
        self.assertEqual(one.zarb(3,'s'),'sss')
        self.assertEqual(one.zarb(-2,3),-6)

    def test_add(self):
        self.assertEqual(one.add(2,3),5)
        self.assertEqual(one.add(-2,3),1)
        self.assertEqual(one.add(-2,-3),-5)
        self.assertEqual(one.add(0,3),3)


    def test_menha(self):
        self.assertEqual(one.menha(2,3),-1)
        self.assertEqual(one.menha(-2,3),-5)
        self.assertEqual(one.menha(0,3),-3)

    def test_taghsim(self):
        self.assertEqual(one.taghsim(10,5),2)
        self.assertEqual(one.taghsim(10,10),1)
        self.assertRaises(ZeroDivisionError,one.taghsim,4,0)


        
if __name__ == "__main__":
    unittest.main()





        

