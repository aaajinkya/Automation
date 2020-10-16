*** Setting ***
Library     SeleniumLibrary
Resource          ../pages/login_page.robot

Force Tags        login     regression

Test Setup      Open Application
Test Teardown   Close Browser


*** Test Cases ***

Valid Login
    Click on login url
    Input Username  test
    Input Password  test
    Click on login
    Title Should Be    User Information - Demo App


Invalid Login
    Click on login url
    Input Username  invalid
    Input Password  test
    Click on login
    Location Should Be    http://localhost:8080/error
    Title Should Be    Login Failure - Demo App
