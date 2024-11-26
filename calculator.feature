Feature: Calculator
    Validate all arithmatic and trigonometric functions

  Scenario: Addition
    Given the calculator is initialized
    When I add 10 and 5
    Then the result should be 15

  Scenario: Subtraction
    Given the calculator is initialized
    When I subtract 10 from 20
    Then the result should be 10

  Scenario: Multiplication
    Given the calculator is initialized
    When I multiply 10 and 5
    Then the result should be 50

  Scenario: Division
    Given the calculator is initialized
    When I divide 10 by 2
    Then the result should be 5

