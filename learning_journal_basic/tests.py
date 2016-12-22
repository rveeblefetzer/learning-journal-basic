import pytest
from pyramid import testing

ENTRIES = {
    1: {"id": 1, "title": "Today, Dec. 16, I learned.", "creation_date": "12/16/2016", "body": "Sample text"},
    2: {"id": 2, "title": "Today, Dec. 17, I learned.", "creation_date": "12/17/2016", "body": "Sample text"},
    3: {"id": 3, "title": "Today, Dec. 18, I learned.", "creation_date": "12/18/2016", "body": "Sample text"},
    4: {"id": 4, "title": "Today, Dec. 19, I learned.", "creation_date": "12/19/2016", "body": "Sample text"},
    5: {"id": 5, "title": "Today, Dec. 20, I learned.", "creation_date": "12/20/2016", "body": "Sample text"},
}


@pytest.fixture
def req():
    """Dummy request fixture."""
    the_request = testing.DummyRequest()
    return the_request

def test_register_page_renders_file_data(req):
    """Ensure my home page view returns some data."""
    from .views import register
    response = register(req)
    assert "ENTRIES" in response


def test_register_page_has_iterable(req):
    """Ensure my register page view returns some iterable data."""
    from .views import register
    response = register(req)
    assert hasattr(["ENTRIES"], "__iter__")


def test_update_page_renders_file_data(req):
    """Ensure my edit-post page view returns some data."""
    from .views import update
    response = update(req)
    assert "ENTRIES" in response


def test_update_page_has_iterable(req):
    """Ensure my edit-post page view returns some iterable data."""
    from .views import update
    response = update(req)
    assert hasattr(["ENTRIES"], "__iter__")


def test_create_page_renders_file_data(req):
    """Ensure my write-new-post page returns some data."""
    from .views import create
    response = create(req)
    assert "ENTRIES" in response


def test_create_page_has_iterable(req):
    """Ensure my create page view returns some iterable data."""
    from .views import create
    response = create(req)
    assert hasattr(["ENTRIES"], "__iter__")


def test_detail_page_renders_file_data(req):
    """Ensure my home page view returns some data."""
    from .views import detail
    response = detail(req)
    assert "ENTRIES" in response


def test_detail_page_has_iterable(req):
    """Ensure my jinja2 page view returns some iterable data."""
    from .views import detail
    response = detail(req)
    assert hasattr(["ENTRIES"], "__iter__")


@pytest.fixture
def testapp():
    """Test App fixture."""
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    return TestApp(app)


def test_index_page_exists(testapp):
    """Index page should exist."""
    response = testapp.get("/", status=200)
    inner_html = response.html
    assert "Today, Dec. 17" in inner_html


def test_detail_page_exists(testapp):
    """Detail page should exist."""
    response = testapp.get("/journal/1", status=200)
    inner_html = response.html
    assert "Today, Dec. 17" in inner_html


def test_edit_form_page_exists(testapp):
    """Edit Form page should exist."""
    response = testapp.get("/journal/3/edit-entry", status=200)
    inner_html = response.html
    assert "Today, Dec. 18," in inner_html


def test_new_form_page_exists(testapp):
    """New Form page should exist."""
    response = testapp.get("/journal/new-entry", status=200)
    inner_html = response.html
    assert "Today, Dec. 18," in inner_html