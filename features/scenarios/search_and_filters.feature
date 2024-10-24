Feature: Search Filters Functionality

  @TC-01 @filter_location
  Scenario: TC-01 Verify the user can select a specific location from the location filter and show correct data
    Given the user is on the home page
    And the user selects wherever button
    When the user selects "New York" from the location filter
    And the user performs the search
    Then the selected location should be "New York"
    And only results from the selected city are displayed
    And the user sees all the properties in the city

  @TC-02 @filter_location
  Scenario: TC-02 Verify the user can select more than one location from the location filter and show correct data
    Given the user is on the home page
    And the user selects wherever button
    When the user selects "New York" from the location filter
    And the user selects "Texas" from the location filter
    And the user performs the search
    Then the selected locations should be "New York" and "Texas"
    And only results from the selected locations are displayed

  @TC-03 @filter_dates
  Scenario: TC-03 Verify the user can select available dates with exact dates and the results make sense
    Given the user is on the home page
    When the user selects Whenever button
    And the user selects the exact dates from the "13"th to the "16"th of the current month
    And the user performs the search
    Then the correct dates should be displayed in the filters
    And the results should be displayed for the selected dates

  @TC-04 @filter_guests
  Scenario: TC-05 Verify that the user can define the number of guests and that the results show properties with the appropriate number of guests.
    Given the user is on the home page
    And the user selects wherever button
    When the user selects "New York" from the location filter
    And the user selects Whoever button
    And the user sets the guest count to "6"
    And the user performs the search
    Then the selected location should be "New York"
    And the selected amount of people is "6"
    And the user only sees properties with the number of people greater than or equal to the selected number of people.
