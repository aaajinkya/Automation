*** Settings ***
Documentation   Generic data
Library           SeleniumLibrary

*** Variables ***
${SERVER URL}            http://localhost:8080
${BROWSER}        Firefox


*** Keywords ***
Open Application
    Open Browser    ${SERVER URL}    ${BROWSER}
    Maximize Browser Window