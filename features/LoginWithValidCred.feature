Feature:Login with Valid credentials

  Scenario:Valid credentials
    Given launch chrome browser
    When open AbcdSchool forum
    Then verify login page with login keyword
    And Enter Username and password
    And Click on login button
    And Verify login successful or not
    And close browser