*** Setting ***
Library     SeleniumLibrary
Resource          ../pages/login_page.robot
Resource          ../pages/register_page.robot

Force Tags        registration     regression

Test Setup      Open Application
Test Teardown   Close Browser


*** Test Cases ***

Register User
    Open Browser  ${SERVER URL}    ${BROWSER}
    Click on register url
    Input Username as       test
    Input Password as       test
    Input Firstname as      first
    Input Lastname as       family
    Input Phone as          123123123
    Click on register
    Click on login url
    Input Username          test
    Input Password          test
    Click on login
    table cell should contain   //table[@id='content']  2   2   test
    table cell should contain   //table[@id='content']  3   2   first
    table cell should contain   //table[@id='content']  4   2   family
    table cell should contain   //table[@id='content']  5   2   123123123


