from external_brain.return_tf_as_a_frozen_set import return_tf_as_a_frozen_set
from external_brain.return_tf_as_a_set import return_tf_as_a_set
import pytest

def test_return_tf_as_a_set():
    
    assert return_tf_as_a_set('a') == {'a'}
    assert return_tf_as_a_set({'a'}) == {'a'}
    assert return_tf_as_a_set(frozenset({'a'})) == {'a'}
    assert return_tf_as_a_set({}) == set()
    
    with pytest.raises(ValueError):
        return_tf_as_a_set(1)

def test_return_tf_as_a_frozen_set():
        
    assert return_tf_as_a_frozen_set('a') == frozenset({'a'})
    assert return_tf_as_a_frozen_set({'a'}) == frozenset({'a'})
    assert return_tf_as_a_frozen_set(frozenset({'a'})) == frozenset({'a'})
    assert return_tf_as_a_frozen_set({}) == frozenset()
    
    with pytest.raises(ValueError):
        return_tf_as_a_frozen_set(1)