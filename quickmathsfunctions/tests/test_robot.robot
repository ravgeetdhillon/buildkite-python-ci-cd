*** Settings ***
Library                quickmathsfunctions/src/quickmathsfunctions.py


*** Test Cases ***
Test Add
    # WHEN
    ${result}=         add      ${10}  ${5}
    # THEN
    Should Be Equal    ${result}     ${15}  

Test Subtract
    # WHEN
    ${result}=         subtract      ${10}  ${-5}
    # THEN
    Should Be Equal    ${result}     ${15}

Test Multiply
    # WHEN
    ${result}=         multiply      ${-10}  ${-5}
    # THEN
    Should Be Equal    ${result}     ${50}

Test Divide
    # WHEN
    ${result}=         divide      ${10}  ${2}
    # THEN
    Should Be Equal    ${result}     ${5}
