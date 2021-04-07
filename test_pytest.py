import pytest
from person import Person
import time

class TestPerson:
    @pytest.fixture
    def setup(self): #run before per test 
        self.p1  = Person("sina","jamshidi")
        self.p2 = Person("surush","jamshidi")
        yield 'setup'
        # after yeild everythings in local function will be teardown
        time.sleep(5)
        #print doesnt work




    def test_fullname(self,setup):
        # p1 = Person("sina","jamshidi")
        # p2 = Person("surush","jamshidi")

        assert self.p1.fullname() == "sina jamshidi"
        assert self.p2.fullname() == "surush jamshidi"

    def test_email(self,setup):

        # p1 = Person("sina","jamshidi")
        # p2 = Person("surush","jamshidi")


        assert self.p1.email() == "sinajamshidi@gmail.com"
        assert self.p2.email() == "surushjamshidi@gmail.com"

