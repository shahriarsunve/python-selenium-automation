# Created by lana at 11/23/24
Feature: Tests for search

  Scenario: User can search for tea
    Given Open target main page
    When Search for Coca Cola
    Then Verify search results shown for Coca Cola
    Then Verify search term coca+cola in URL

  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search results shown for coffee

  Scenario: User can search for a mug
    Given Open target main page
    When Search for a mug
    Then Verify search results shown for a mug

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <product>
    Examples:
    |product    |
    |coffee     |
    |tea        |
    |mug        |

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image

  Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown