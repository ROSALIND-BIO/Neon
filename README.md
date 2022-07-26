We’re building the app with [FastAPI](https://fastapi.tiangolo.com/), a modern and high-performance web framework for building web apps based on standard Python type hints. I would highly recommend you check out the docs for FastAPI, as they’re some of the best library docs I’ve ever seen

# Commands

You can run commands from any directory in the repository. The most common workflows are to either run these commands from the root of the repository or from the `/scripts` directory. This assumes you’re in the `/scripts` directory.

- `./run.sh` - Start the API in local development mode. This will populate the database using scripts from the `/setup` directory
- `./clean.sh` - Run linting tools on the entire repo. Currently, this includes…
    - [isort](https://pycqa.github.io/isort/) - Sort imports according to PEP 8 standards
    - [black](https://black.readthedocs.io/en/stable/) - An opinionated code formatter

# Windows Tooling

1. Download and set up your IDE
    1. [PyCharm](https://www.jetbrains.com/pycharm/)
    2. [VS Code](https://code.visualstudio.com/)
2. Download and install [Anaconda](https://www.anaconda.com/products/individual)
    1. Check the `Add Anaconda to my PATH environment variable` checkbox
    2. Check the `Register Anaconda as my default Python 3.X` checkbox
3. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop)
    1. The download link will download an installer, not the full app
    2. To install Docker Desktop properly, right click the downloaded installer and click `Run as administrator`. This will install Docker Desktop
    3. You also need a Linux kernel update package, which you can download and install from [here](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package). You must follow steps 4 and 5
        1. Step 4 is to download and install the latest package
        2. Step 5 is to set WSL 2 as your default version
4. Restart your computer
5. Follow the standard setup instructions below

# Setup

These instructions assume you have Anaconda and Docker installed on your local machine. If you’re having issues installing these tools or need assistance, please reach out to [Fletcher](https://onrampbio.slack.com/archives/D029NFC9C2G).

1. Download the GitHub repo
    1. `git clone git@github.com:ROSALIND-BIO/Iron.git`
    2. `cd Iron` (or whatever commands you need to change directories into the root of the repo)
2. Set up a new Anaconda environment
    1. `conda create -n Iron python=3.10`
    2. `conda activate Iron`
    3. `pip install -r requirements.txt`
3. Add your Anaconda environment to your IDE as an interpreter
    1. [PyCharm](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360006880560-How-add-an-already-existed-conda-environment-to-pycharm-as-an-interpreter-)
        1. You likely want to install the [Pydantic plugin](https://koxudaxi.github.io/pydantic-pycharm-plugin/) as well
    2. [VS Code](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
4. Start Docker Desktop (may take a minute or more to start up)
5. Run `./scripts/run.sh` to ensure everything starts up and works as expected
    1. This will run the app (and other containers) in Docker, and will start the server on localhost:8000
    2. You can visit [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/login](http://localhost:8000/login) to ensure the app is running
    3. If you’ve got a SQL workbench tool installed (such as [Postico 2](https://eggerapps.at/postico2/) or [pgAdmin](https://www.pgadmin.org/)), you can access the database on [localhost](http://localhost/) port 5432 (check `docker/Local.compose.yaml` for database credentials)

# Tools

- [HTMX](https://htmx.org/)
- [Material Design Bootstrap](https://mdbootstrap.com/) + [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
    - Contact [Fletcher](https://onrampbio.slack.com/archives/D029NFC9C2G) for login credentials to MDB Pro
- [jQuery](https://jquery.com/)
- [Material Design Icons](https://materialdesignicons.com/)
- [FastAPI [and related resources]](https://fastapi.tiangolo.com/)
  - [Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/)
  - [Form Data](https://fastapi.tiangolo.com/tutorial/request-forms/)
  - [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
  - [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
  - [Body Fields](https://fastapi.tiangolo.com/tutorial/body-fields/)
  - [Jinja2](https://fastapi.tiangolo.com/advanced/templates/#using-jinja2templates)
  - [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Django ORM](https://docs.djangoproject.com/en/4.0/topics/db/queries/)
- [Python Data Classes](https://docs.python.org/3/library/dataclasses.html)
