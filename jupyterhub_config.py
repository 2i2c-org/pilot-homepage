import pathlib
from oauthenticator.generic import GenericOAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner


c.JupyterHub.spawner_class = SimpleLocalProcessSpawner

HERE = pathlib.Path(__file__).parent

c.JupyterHub.template_paths = [str(HERE / 'templates')]

c.JupyterHub.authenticator_class = GenericOAuthenticator

c.Authenticator.admin_users = [
    'yuvipanda'
]

c.JupyterHub.template_vars = {
    'hub': {
        'org_name': 'University of Foo',
        'org_logo': 'https://jupyter.org/assets/nav_logo.svg',
        'org_url': 'https://jupyter.org',
    }
}
