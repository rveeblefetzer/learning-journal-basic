def includeme(config):
    """Add routes to Pyramid's Configurator."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('write', '/journal/new-entry')
    config.add_route('edit', '/journal/{id:\d+}/edit-entry')

    # Routes to connect to proper pages for assignment#
    config.add_route('assignment_entry', '/entry.html')
    config.add_route('assignment_write', '/write.html')
    config.add_route('assignment_edit', '/editentry.html')
