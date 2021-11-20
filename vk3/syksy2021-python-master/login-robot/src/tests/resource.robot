*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

#Input New Command
    #[Arguments]  ${arg0}
    #Input  ${arg0}

Input New Command
    Input  new

    