*** Settings ***

Resource    common.robot



*** Keywords ***
Click on register url
    Click Link     //a[contains(text(),'Register')]


Input username as
    [Arguments]    ${username}
    Input Text    username    ${username}

Input password as
    [Arguments]    ${password}
    Input Text    password    ${password}

Input firstname as
    [Arguments]    ${firstname}
    Input Text    firstname   ${firstname}

Input lastname as
    [Arguments]    ${lastname}
    Input Text     lastname    ${lastname}

Input phone as
    [Arguments]    ${phone}
    Input Text     phone       ${phone}


Click on register
    Click Button    //input[@value='Register']