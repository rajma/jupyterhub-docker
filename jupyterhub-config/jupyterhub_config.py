from nativeauthenticator import NativeAuthenticator
from dockerspawner import DockerSpawner
import os


c.JupyterHub.spawner_class = DockerSpawner
#  Use SQLite
c.JupyterHub.db_url = "sqlite:////srv/jupyterhub/jupyterhub.sqlite"  # Store in the jupyterhub-data volume
# c.NativeAuthenticator.create_system_users = True

c.JupyterHub.authenticator_class = NativeAuthenticator
c.JupyterHub.admin_access = True
c.Authenticator.allowed_users = {"rajma", "annaic"}
c.Authenticator.admin_users = {"rajma", "annaic"}
c.Authenticator.allow_all = True


c.JupyterHub.hub_ip = '0.0.0.0'
# c.JupyterHub.hub_bind_url = 'http://0.0.0.0:8000'
c.DockerSpawner.image = 'jupyter/minimal-notebook:latest'
c.DockerSpawner.network_name = 'jupyterhub-network'
c.DockerSpawner.volumes = {
    'jupyterhub-user-{username}': '/home/jovyan/work',
}

# Add these lines:
c.DockerSpawner.uid = 1000
c.DockerSpawner.gid = 1000



c.JupyterHub.cookie_secret = os.urandom(32)
