@Agrostartest

Feature: Test cases for Git API

@gitcreate
Scenario Outline: Create repo via API, star the repo and verify details
    Given create git repo with name <repo_name>
    When star the created repo and verify
    Then get repo details and verify
    Examples:
    | repo_name |
    | Test_repo |