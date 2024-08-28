c = get_config()

# Set the JupyterHub IP
c.JupyterHub.ip = '0.0.0.0'

# Set the post JypyterHub listens on
c.JupyterHub.port = 8000

# Authentication mechanism (can be changed to OAuth, etc.)
c.Authenticator.admin_users = {'admin'}

# DockerSpawner or KubeSpawner can be used if needed


