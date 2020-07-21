from . import development, testing, production


def set_app_config_keys(app, settings):
    """Load all flask.Flask config vars."""
    # create a unique dict with all config vars
    all_config_vars = dict(
        list(settings.FLASK_VARS.items())
    )

    for key, value in all_config_vars.items():
        app.config[key] = value


def development_config(app):
    set_app_config_keys(app, development)


config = {
    'development': development_config,
    'default': development_config,
}
