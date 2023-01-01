# from typing import List
import pytest


@pytest.fixture(scope="module")
def src() -> str:
    return "examples/data/acc4000.tif"
