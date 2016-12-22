def includeme(config):
    """All of the routes for the configuration to find."""
    config.add_static_view(name='static', path='learning-journal-basic:static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('form', '/journal/new-entry')
    config.add_route('edit_form', '/journal/{id:\d+}/edit-entry')
