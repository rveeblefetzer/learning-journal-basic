def includeme(config):
    """Add routes to Pyramid's Configurator."""
    config.add_static_view(name='static', path='learning_journal_basic:static', cache_max_age=3600)
    config.add_route('homepage', '/')
    config.add_route('detail', 'journal/{id:\d+}')
    config.add_route('write', 'journal/write')
    config.add_route('edit', 'journal/{id:\d+}/editentry')
