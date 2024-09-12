import pytest
import fonctions as f

def test_1 ( ) :
	assert f.puiss (2 ,3) == 8
	assert f.puiss (2 ,2) == 4
	
def test_2 ( ) :
	assert f.puiss (-2 ,3) == -8
	assert f.puiss (-2 ,2) == 4
	assert f.puiss (2 ,-2) == 0.25
	assert f.puiss (2 ,-3) == 0.125
	
def test_3 ( ) :
	assert f.puiss (0 ,0) == 1
	assert f.puiss (0 ,5) == 0
	assert f.puiss (5 ,0) == 1
	assert f.puiss (10 ,5) == 100000
	assert f.puiss (3.4,-4.1) == 0.00662119594
