import pytest
import warnings


def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn('my warning', UserWarning)
