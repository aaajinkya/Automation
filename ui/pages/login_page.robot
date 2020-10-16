*** Settings ***

Resource    common.robot


*** Keywords ***
Click on login url
    Click Link     //a[contains(text(),'Log In')]

Input Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Click on login
    Click Button    //input[@value='Log In']

Logout from Application
    Click Link     /a[contains(text(),'Log Out')]


Login Page Should Be Open
    Title Should Be    index page - Demo App
