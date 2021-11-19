*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials  kalle  salasana
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  mikko  salasana
    Output Should Contain  Invalid username or password

##Register With Valid Username And Password
# ...

##Register With Already Taken Username And Valid Password
# ...

##Register With Too Short Username And Valid Password
# ...

##Register With Valid Username And Too Short Password
# ...

##Register With Valid Username And Long Enough Password Containing Only Letters
# ...


*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command


