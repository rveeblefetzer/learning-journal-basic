import pytest
from pyramid import testing

@pytest.fixture
def req():
    the_request = testing.DummyRequest()
    return the_request


# def test_home_page_renders_file_data(req):
#     """My homepage view returns data."""
#     from .views import home_page
#     response = home_page(req)
#     assert

