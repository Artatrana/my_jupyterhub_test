# Use the offical JupyterHub base image
FROM jupyterhub/jupyterhub:1.4.2

# Install additional package if needed
RUN pip install notebook jupyterlab

# Copy JupyterHub config
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# Expose port 8000 for JupyterHub
EXPOSE 8000

CMD ["jupyterhub", "-f","/srv/jupyterhub/jupyterhub_config.py"]

