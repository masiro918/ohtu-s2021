*** Settings ***
Resource  resource.robot
Test Setup  Create Test User

*** Test Cases ***

Register With Valid Username And Password
    Input New Command
    Input  kalle
    Input  kissakoira1
    Run Application
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input  testitimo
    Input  kissakoira1
    Run Application
    Output Should Contain  Username is already exists!

Register With Too Short Username And Valid Password
    Input New Command
    Input  ki
    Input  kissakoira1
    Run Application
    Output Should Contain  Username is too short!


Register With Valid Username And Too Short Password
    Input New Command
    Input  testi
    Input  kissa
    Run Application
    Output Should Contain  Password is too short!

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input  testiteemu
    Input  kissakoira
    Run Application
    Output Should Contain  Password is not valid!

*** Keywords ***
Create Test User
    Input New Command
    Input  testitimo
    Input  kissakoira1
