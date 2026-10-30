# language: en
Feature: Enable the Export button

  Scenario: The Export button is disabled when there are no products with data
    Given a dashboard with no products with loaded data
    When the user opens the reports screen
    Then the Export button should be disabled

  Scenario: The Export button is enabled when there is at least one product with data
    Given a dashboard with 1 product with loaded data
    When the user opens the reports screen
    Then the Export button should be enabled
