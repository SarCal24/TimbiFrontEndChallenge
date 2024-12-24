@regression_tests
Feature: Validate element created dropdown column

  Scenario: Navigate to the Kayak home page and validate principal elements
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The page "should" contain the next elements
      | name                   | type   |
      | name_tag               | input  |
      | name_dropdown_column   | input  |
      | search_tag             | input  |
      | cancel                 | button |
      | create_column_disabled | button |

  Scenario: Validate URL of Home page
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The url page should contains the next "https://www.kayak.com"  in the url

  Scenario Outline: Navigate between countries and validate the URL
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I navigate to the "<url>" URL
    Then The url page should be equal to the next "<url>" url

    Examples:
      | url                       |
      | https://www.kayak.com.my/ |
      | https://www.kayak.com.pr/ |
      | https://www.kayak.com.br/ |


  Scenario Outline: Navigate to the Kayak and validate options with url changes
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I click on the "main_navigation" "button"
    And I click on the "<element_name>" "button"
    Then The url page should contains the next "<element_name>"  in the url

    Examples:
      | element_name |
      | flights      |
      | stays        |
      | cars         |
      | explore      |
      | news         |
      | business     |
      | trip         |

  Scenario Outline: Navigate to the Kayak and validate options with dropdown menus
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I click on the "main_navigation" "button"
    And I click on the "<element_name>" "button"
    Then The "area_expanded" "button" "should" be enabled

    Examples:
      | element_name |
      | language     |
      | currency     |