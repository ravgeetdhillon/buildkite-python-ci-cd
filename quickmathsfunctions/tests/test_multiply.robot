# 1
*** Settings ***
Library                quickmathsfunctions/src/quickmathsfunctions.py


*** Test Cases ***
Multiplication of Positive Numbers
    # WHEN
    ${result}=         multiply      ${10}  ${5}
    # THEN
    Should Be Equal    ${result}     ${50}  

Multiplication of Positive and Negative Numbers
    # WHEN
    ${result}=         multiply      ${10}  ${-5}
    # THEN
    Should Be Equal    ${result}     ${-50}

Multiplication of Negative Numbers
    # WHEN
    ${result}=         multiply      ${-10}  ${-5}
    # THEN
    Should Be Equal    ${result}     ${50}

Multiplication with Zero
    # WHEN
    ${result}=         multiply      ${10}  ${0}
    # THEN
    Should Be Equal    ${result}     ${0}
