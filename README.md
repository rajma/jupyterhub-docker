# JupyterHub with Docker

This repository provides a Docker-based setup for running JupyterHub, a multi-user hub that spawns single-user Jupyter Notebook servers.

## Features

* **Dockerized:** Runs JupyterHub and its components in Docker containers for easy setup and deployment.
* **Scalable:** Can be scaled to support multiple users.
* **Customizable:** Provides flexibility to configure JupyterHub and user environments.
* **SQLite:** Configured to use SQLite.

## Prerequisites

* [Docker](https://docs.docker.com/get-docker/) installed on your system.
* [Docker Compose](https://docs.docker.com/compose/install/) installed on your system.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/rajma/jupyterhub-docker.git](https://www.google.com/search?q=https://github.com/rajma/jupyterhub-docker.git)
    cd jupyterhub-docker
    ```

2.  **Create a `.env` file:**
    * Create a file named `.env` in the same directory as `docker-compose.yml`.
    * Add the following line to generate a secure cookie secret:

        ```bash
        JUPYTERHUB_COOKIE_SECRET=$(python -c 'import secrets; print(secrets.token_hex(32))')
        ```

3.  **Start JupyterHub:**

    ```bash
    docker-compose up --build
    ```

    This command will build the necessary Docker image and start the JupyterHub container in detached mode.

## Configuration

JupyterHub is configured using the `jupyterhub_config.py` file. This repository provides a default configuration, but you can customize it as needed.

* `jupyterhub_config.py`:  Contains the JupyterHub configuration, including authentication, spawning, and networking.  Key settings include:
    * `c.JupyterHub.authenticator_class`:  Configures the authentication method (e.g., `NativeAuthenticator`).
    * `c.JupyterHub.spawner_class`:  Configures how user servers are spawned (e.g., `DockerSpawner`).
    * `c.JupyterHub.hub_ip` and `c.JupyterHub.hub_bind_url`:  Configure the network address and port for JupyterHub.
    * `c.DockerSpawner.image`: Specifies the Docker image to use for user servers.
    * `c.NativeAuthenticator.db_url`: Configures the SQLite database location.

## Usage

1.  **Access JupyterHub:** Open your web browser and go to `http://localhost:8000`.
2.  **Log in:**
    * Create user called "rajma" as the username and create a password. Login with this user.

## Docker Compose File (`docker-compose.yml`)

The `docker-compose.yml` file defines the services, networks, and volumes for the JupyterHub deployment.

* `services`: Defines the `jupyterhub` service, specifying the Dockerfile, ports, volumes, environment variables, and network.
* `volumes`:  Defines the `jupyterhub-data` volume for persistent storage of user data and the SQLite database.
* `networks`:  Defines the `jupyterhub-network` for communication between the JupyterHub container and user servers.

## Dockerfile

The `Dockerfile` is used to build the JupyterHub Docker image. It starts from the official JupyterHub image and installs any additional dependencies.

## Data Persistence

The `jupyterhub-data` volume is used to persist:

* User data
* SQLite database

This ensures that user data and the database are preserved across container restarts.

## Security Notes

* **Cookie Secret:** The `JUPYTERHUB_COOKIE_SECRET` environment variable is used to set a secret key for securing cookies.  It is crucial to keep this value secure.  The provided installation instructions use a randomly generated secret.
* **Authentication:** This setup uses `NativeAuthenticator`, which stores user credentials in a local SQLite database. For production deployments, consider using a more robust authentication method (e.g., OAuth, LDAP).
* **Admin User**: The first user to sign up is the admin user.

## Troubleshooting

* **Port Conflict:** If you encounter an error that the port 8000 is already in use, make sure that no other application is using this port.
* **Permission Issues:** Ensure that the `jupyterhub-data` directory is writable by the Docker container.
* **Configuration Errors:** Double-check the `jupyterhub_config.py` file for any typos or syntax errors.
* **Rebuild:** If you make any changes to the `Dockerfile` or `jupyterhub_config.py`, make sure to rebuild the image using  `docker-compose build --no-cache`

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit a pull request or open an issue.
