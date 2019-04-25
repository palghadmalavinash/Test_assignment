import pytest
import random
from pytest_bdd import (
    given,
    scenarios,
    when,
    then,
)

from src.pages.Git_API import git_api as gAPI

scenarios("../../feature/Git_API/git_api.feature")


@pytest.fixture()
def git_api():
    git_api=gAPI.git_api()
    return git_api


@given("create git repo with name <repo_name>")
@pytest.fixture()
def create_repo(git_api,repo_name):
    """
    function to create repo on Git
    :param git_api: git_api object
    :param repo_name: Name of the repo to be created
    :return: response Status
    """
    rand_no=random.randint(1,999)
    repo=repo_name+str(rand_no)
    status = git_api.create_rep(repo)
    assert status.status_code == 201
    return status


@when("star the created repo and verify")
def star_repo(git_api,create_repo):
    """
    Function to star the created repo.
    :param git_api: git_api object
    :param create_repo: Response of create repo request.
    :return: None
    """
    status = git_api.star_repo(create_repo)
    assert status.status_code == 204


@then("get repo details and verify")
def verify_repo(git_api,create_repo):
    """
    Verify the repo is created and starred
    :param git_api: git_api object
    :param create_repo: Response of create repo request
    :return: None
    """
    result = git_api.validate_repo(create_repo)
    assert result == True