import pytest
import one

class TestOne():
    
    def test_zarb(self):
        assert one.zarb(3,5) == 15
        assert one.zarb(3,0) == 0 
        assert one.zarb(3,'s') == 'sss'
        
    