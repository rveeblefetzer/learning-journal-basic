def includeme(config):
    """Add routes to Pyramid's Configurator."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('homepage', '')
    config.add_route('detail', 'journal/{id:\d+}.{html}')
    """Route above for assignment-only page to edit entry.
    It's a kludge to overall design."""
    config.add_route('write', 'journal/write.{html}')
    config.add_route('edit', 'journal/{id:\d+}/editentry.{html}')
