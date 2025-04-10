# Template Repo

[![PyPI](https://img.shields.io/tpypi/v/repo-template.svg)](https://test.pypi.org/project/repo-template)
[![pytest](https://github.com/jorgemarpa/repo-template/actions/workflows/pytest.yaml/badge.svg)](https://github.com/jorgemarpa/repo-template/actions/workflows/pytest.yaml/) [![mypy](https://github.com/jorgemarpa/repo-template/actions/workflows/mypy.yaml/badge.svg)](https://github.com/jorgemarpa/repo-template/actions/workflows/mypy.yaml) [![ruff](https://github.com/jorgemarpa/repo-template/actions/workflows/ruff.yaml/badge.svg)](https://github.com/jorgemarpa/repo-template/actions/workflows/ruff.yaml)[![Docs](https://github.com/jorgemarpa/repo-template/actions/workflows/deploy-mkdocs.yaml/badge.svg)](https://github.com/jorgemarpa/repo-template/actions/workflows/deploy-mkdocs.yaml)

This is a template repository ready to develop code. It uses poetry to manage dependencies, python environment, and packaging. Flake8 and Black to format code. Mkdocs to create documentation from docstring. And adds GitHub actions to automatize tasks.

## Poetry

[Poetry](https://python-poetry.org/docs/) helps you to manage a python package project. It manage dependencies, versions, and python environments. 
First initialize a project:

```
poetry new --src <repo-name>
```

This will create a new `repo-name` directory with default files and folders.
We use the `--src` flag to use the source folder layout.
In the repo directory we can add new dependencies with:

```
poetry add numpy matplotlib pandas
```

To install the ne package in a virtual env we can do:

```
poetry install
```
and to run other commands using the python env, e.g. `pytest`, we can do:

```
poetry run pytest...
```

To release and publish our package with poetry in PyPi we use:
```
poetry build
```
this will create the wheel files and package the repository in the `dist` folder
Then after creating a new package in PyPi website and setting up the token we configure this into poetry:

```
poetry config pypi-token.pypi <token>
```
and then we publish with:
```
poetry publish
```
This will upload the package to the index. We will do this every time there is a new major or minor version of our package. This can be done also as a GitHub action, will add that later.


## GitHub

Initialize Git repository and sync with GitHub:
In the project directory do
```
git init
```
to initialize the Git repo. Now we can add changes and commit to the main branch and sync with GitHub.

```
git add *
git commit -m "first commit"
git remote add origin <GITHUB url>
git push -u origin main
```
More info [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories?tool=webui).

## MkDocs

To create a documentation page using the docstring in our code we will use `mkdocs` [website](https://docs.readthedocs.io/en/stable/intro/getting-started-with-mkdocs.html).
First, install the library in the virtual env:
```
poetry add -G dev mkdocs mkdocstrings mkdocs-material
```

Now we can initialize MkDocs with:
```
poetry run mkdocs new .
```
This will create the configuration file and docs folder to add to our page.

To build the documentation as a page we use:
```
poetry run mkdocs build
poetry run mkdocs serve
```
This will build the documentation and create a local view of the page to visualize in our browser.


Additionally, we need to give permission to GitHub to deploy the website from the repository branch.
We do this by going to the configuration's page of the repository and in the "Pages" tab on the left
we update the source to "Deploy from a branch" and change the branch to "gh-pages" in the "/root" directory.
To deploy the the page to Github branch with the documentation we do
```
poetry run mkdocs gh-deploy
```
this will create the website [https://jorgemarpa.github.io/repo-template/](https://jorgemarpa.github.io/repo-template/) which has the documentation we have created.

As an extra step, we can add a quick link to the repo page in the "About" section of the landing page of our repository.


## Pytest

Pytest will run any test code that is written in the `tests` folder. Ideally we want to test all our code to ensure nothing breaks and that function behavior is as expected. We can run `pytest` locally before committing to the branch or PR with:
```
poetry run pytest -v tests
```

## GitHub Actions

This are automatic actions that happens during pushing new commits and/or pull request. We can configure these actions in a `yaml` file in the `.github/workflows` directory. These actions automatize most of the routine steps described in this document. 

In this template we have the following workflows: 
 
 - `ruff`: does code formatting, lint, and sorting. It replaces `flake8`, `isort`, and `black`.
 -  `deploy-mkdocs`: creates documentation page from with Mkdocs.
 -  `pytest`: runs python test
 -  `dependabot`: check for security and version updates of project dependencies and creates PRs when new version are available.
 -  `mypy`: check for python static programming. 
 -  `pypi-publish`: published the project in PyPI when a new GitHub release/tag is created

### Publish to PyPI Action

This repo has the action `pypi-publish.yaml` that automatically publish the package to TestPyPI once a 
release or a tag version is created in GitHub. Note that for this example we used 
[TestPyPI](https://test.pypi.org/) which is an instance of PyPI to test package deployment and publishing 
without affecting the real index. It is ideal to test things. 
We also need to setup a TestPyPI/PyPI API token and add it to GitHub secrets.

When our package is ready to be publish to the real PyPI, we need to update the action as follows:
```
- name: Config Poetry to testPyPI
        run: |
          poetry config repositories.test-pypi https://test.pypi.org/legacy/
          poetry config pypi-token.test-pypi "${{ secrets.TEST_PYPI_API_KEY }}"
- name: Publish package to testPyPI
        run: poetry publish -r test-pypi --build
```
to 
```
- name: Config Poetry to PyPI
        run: |
          poetry config pypi-token.pypi "${{ secrets.PYPI_API_KEY }}"
- name: Publish package to testPyPI
        run: poetry publish --build
```
This will change te repository configuration back to publish to PyPI. Remember to add the PyPI
API token to GitHub secrets.

See this [tutorial](https://www.ianwootten.co.uk/2020/10/23/publishing-to-pypi-using-github-actions/) for more details.