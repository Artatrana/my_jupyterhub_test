# JupyterHub on Google Kubernetes Engine (GKE)

This project deploys a JupyterHub instance on Google Kubernetes Engine (GKE).

## Setup

1. **Build and push the Docker image:**
   ```bash
   docker build -t jupyterhub .
   docker tag jupyterhub gcr.io/[PROJECT-ID]/jupyterhub:latest
   docker push gcr.io/[PROJECT-ID]/jupyterhub:latest
