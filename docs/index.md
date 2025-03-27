# Template Repo

This is a template repository ready to develop code. It uses poetry to manage dependencies, python environmnet, and packagaing. Flake8 and Black to format code. Mkdocs to create documentation from docstrings. And adds GitHub actions to automitize tasks.

## Poetry

[Poetry](https://python-poetry.org/docs/) helps you to manage a python ppackage project. It manage dependencies, versions, and python environments. 
First initialize a project:

```
poetry new --src <repo-name>
```

This will create a new `repo-name` directory with default files and folders.
We use the `--src` flag to use the source folder layout.
In the repo directory we can add new dependencies with:

```
poetry add nympy matplotlib pandas
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
This will upload the package to the index. We will do this everytime there is a new major or minor version of our package. This can be done also as a GitHub action, will add that later.


## GitHub

Initialize Git repository and sync with GitHub:
In the poejct directory do
```
git init
```
to initialize the Git repo. Now we can add changes and commit to the main branch and sync with GitHub.

```
git add *
git commit -m "first comit"
git remote add origin <GITHUB url>
git push -u origin main
```
More info [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories?tool=webui).

## MkDocs

To create a documentation page using the docstrings in our code we will use `mkdocs` [wesite](https://docs.readthedocs.io/en/stable/intro/getting-started-with-mkdocs.html).
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
This will build the documentation and creater a local view of the page to visualize in our browser.

TO deploy the the page to Github branch with the documentation we do
```
poetry run mkdocs gh-deploy
```
this will create the website [https://jorgemarpa.github.io/repo-template/](https://jorgemarpa.github.io/repo-template/) which has the documentation we have created.

## GitHub Actions

This are automatic actions that happens during pushing new commits and/or pull request. We can configure these actions in a `yml` file in the `.github/workflows` directory.
In this template we have one for `ruff`, `deploy-mkdocs`, `pytest`, and `dependabot`. 

## Pytest

Pytest will run any test code that is written in the `tests` folder. Idially we want to test all our code to ensure nothing breaks and that function behavior is as expected. We can run pytest locally before commiting to the branch or PR with:
```
poetry run pytest -v tests
```