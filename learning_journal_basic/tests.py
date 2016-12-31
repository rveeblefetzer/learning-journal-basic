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
    return testing.DummyRequest()


def test_homepage_renders_file_data(req):
    """Ensure my homepage view returns some data."""
    from .views import homepage
    response = homepage(req)
    assert "ENTRIES" in response


def test_homepage_page_has_iterable(req):
    """Ensure my homepage view returns some iterable data."""
    from .views import homepage
    response = homepage(req)
    assert hasattr(["ENTRIES"], "__iter__")


# def test_edit_page_renders_file_data(req):
#     """Ensure my edit-post page view returns some data."""
#     from .views import edit
#     response = edit(req)
#     assert "ENTRIES" in response


# def test_update_page_has_iterable(req):
#     """Ensure my edit-post page view returns some iterable data."""
#     from .views import edit
#     response = edit(req)
#     assert hasattr(["ENTRIES"], "__iter__")


def test_write_page_renders_file_data(req):
    """Ensure my write-new-post page returns some data."""
    from .views import write
    response = write(req)
    assert "ENTRIES" in response


def test_write_page_has_iterable(req):
    """Ensure my create page view returns some iterable data."""
    from .views import write
    response = write(req)
    assert hasattr(["ENTRIES"], "__iter__")


# def test_detail_page_renders_file_data(req):
#     """Ensure my home page view returns some data."""
#     from .views import detail
#     response = detail(req)
#     assert "ENTRIES" in response


# def test_detail_page_has_iterable(req):
#     """Ensure my jinja2 page view returns some iterable data."""
#     from .views import detail
#     response = detail(req)
#     assert hasattr(["ENTRIES"], "__iter__")


@pytest.fixture
def testapp():
    """Test App fixture."""
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    return TestApp(app)


def test_index_page_exists(testapp):
    """Homepage should exist."""
    response = testapp.get("/", status=200)
    html = response.html
    assert "An index of entries." in html.find('header').text


def test_detail_page_exists(testapp):
    """Detail page should exist."""
    response = testapp.get("/journal/1", status=200)
    html = response.html
    assert "The what and the how of the day." in html.find('header').text


def test_edit_form_page_exists(testapp):
    """Edit page should exist."""
    response = testapp.get("/journal/3/editentry", status=200)
    html = response.html
    assert "Make amends. Add, correct, extend." in html.find('header').text


def test_write_page_exists(testapp):
    """New Form page should exist."""
    response = testapp.get("/journal/write", status=200)
    html = response.html
    assert "Reflect, record. What got learned?" in html.find('header').text
