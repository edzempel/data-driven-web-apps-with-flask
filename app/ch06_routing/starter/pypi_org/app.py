import os
import sys
import flask

import pypi_org.services.package_service as package_service

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from pypi_org.infrastructure.view_modifiers import response

app = flask.Flask(__name__)


def main():
    register_blueprints()

    app.run(debug=True)


def register_blueprints():
    from pypi_org.views import home_views
    from pypi_org.views import package_views
    from pypi_org.views import cms_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


if __name__ == '__main__':
    main()
