# learning-journal-basic

A learning journal for Code Fellows' Python 401 class. 

Uses [Start Bootstrap](http://startbootstrap.com/) - [Clean Blog](http://startbootstrap.com/template-overviews/clean-blog/)

This is version step2 using jinja2 templates; site is deployed on Heroku [here](https://learning-journal-step2.herokuapp.com/).

##Routes used:

`config.add_static_view('static', 'static', cache_max_age=3600)`: For serving static files such as CSS and images.

`config.add_route('homepage', '')`: For serving up homepage at root URL. Could not get this to work linking to an explicit index.html and /.

`config.add_route('detail', 'journal/{id:\d+}.{html}')`: For serving a specific journal entry.

`config.add_route('write', 'journal/write.{html}')`: For giving a page to write a new journal entry.

`config.add_route('edit', 'journal/{id:\d+}/editentry.{html}')`: For editing a journal entry.


##Views used:

`homepage`: For retrieving the homepage, giving a list of journal entries.

`detail`: For delivering a specific journal entry. Currently hard-coded to give the newest entry.

`write`: For a page to write a new journal entry.

`edit`: For a page to edit an exisiting journal entry.

These methods were refactored to conflate the open, join and read methods for constructing the URL. Thanks to TA [David Smith](https://github.com/Bl41r), who did it in his learning journal [here](https://github.com/Bl41r/learning-journal-python/blob/step1/website/views.py).

For this assignment, views also has a global ENTRIES variable, a list of sample journal entries in dictionary form.

##Note on tests:
All 8 tests working in py.test; tox, however, can't seem to import webtest, breaking those tests. Coverage report nonexistent.