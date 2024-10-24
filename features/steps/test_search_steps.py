import os

import pytest
from pytest_bdd import given, scenarios, then, when, parsers
from features.pages.home_page import HomePage

scenarios(os.path.join(os.path.dirname(__file__), '../scenarios/search_and_filters.feature'))

@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@given('the user is on the home page')
def step_given(home_page):
    home_page.navigate()
    
    
@given('the user selects wherever button')
def step_given(home_page):
    home_page.click_on_wherever_button()
    
@when(parsers.parse('the user selects "{city}" from the location filter'))
def step_when(home_page, city):
    
    home_page.select_location(city)

@when('the user performs the search')
def step_when(home_page):
    home_page.click_on_search_button()
    
@then(parsers.parse('the selected location should be "{location}"'))
def step_then(home_page, location):
    home_page.verify_city_is_selected(location)
    
@then('only results from the selected city are displayed')
def step_then(home_page):
    home_page.verify_all_cities_are_correct()

@then('the user sees all the properties in the city')
def step_then(home_page):
  home_page.verify_number_of_properties()

@then(parsers.parse('the selected locations should be "{city_one}" and "{city_two}"'))
def step_then(home_page, city_one, city_two):
    home_page.verify_cities_are_selected(city_one, city_two)

@then('only results from the selected locations are displayed')
def step_then(home_page):
    home_page.verify_all_the_cities_are_correct()
    
@when('the user selects Whenever button')
def step_when(home_page):
    home_page.click_on_whenever_button()
    
@when(parsers.parse('the user selects the exact dates from the "{date_one}"th to the "{date_two}"th of the current month'))
def step_when(home_page, date_one, date_two):
    home_page.select_dates(date_one, date_two)

@then('the correct dates should be displayed in the filters')
def step_then(home_page):
    home_page.verify_filter_date_is_correct()
    
@then('the results should be displayed for the selected dates')
def step_then(home_page):
    home_page.verify_correct_date_of_the_results()

@when('the user selects Whoever button')
def step_when(home_page):
    home_page.click_on_whoever_button()
    
@when(parsers.parse('the user sets the guest count to "{guests}"'))
def step_when(home_page, guests):
    home_page.click_on_plus_button_in_whoever(guests)

@then(parsers.parse('the selected amount of people is "{guests}"'))
def step_then(home_page, guests):
   home_page.verify_amount_of_guests_selected(guests)

@then('the user only sees properties with the number of people greater than or equal to the selected number of people.')
def step_then(home_page):
    home_page.verify_guests_number()
    