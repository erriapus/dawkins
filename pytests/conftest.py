# -*- coding: utf-8 -*-
import pytest

@pytest.fixture(scope="module")
def inputs(request):
    return [6, 7, 8, 4, 5]
