Feature:Login with Invalid credentials

  Scenario:Invalid credentials
    Given launch chrome browser
    When open AbcdSchool forum
    Then verify login page with login keyword
    And Enter wrong Username and password
    And Click on login button
    And Verify login is unsuccessful
    And close browser