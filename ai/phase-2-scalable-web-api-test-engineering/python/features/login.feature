Feature: Enterprise Login
  Scenario: Valid credentials
    Given user navigates to login page
    When user enters valid username and password
    Then dashboard should be displayed

  Scenario: Invalid credentials
    Given user navigates to login page
    When user enters invalid username or password
    Then error message should be displayed

  Scenario: Empty credentials
    Given user navigates to login page
    When user leaves username and password empty
    Then validation error should be shown
