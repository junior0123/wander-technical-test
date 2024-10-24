from datetime import datetime
from playwright.sync_api import Page, expect

from config.selectors.home_page_selectors import HomePageButtonSelectors, HomePageCitySelectors
from config.properties_data import PropertiesData
from utils.utils import scroll_to_city, scroll_to_bottom
from config.logger_config import setup_logger
logger = setup_logger()
class HomePage:
    """
    A page object class that represents the Wander website homepage.
    Provides methods to interact with and verify elements on the home page,
    including search filters, location selection, and results verification.
    """
    
    def __init__(self, page: Page):
        """
        Initialize HomePage with a Playwright page object.

        Args:
            page (Page): The Playwright page instance to interact with
        """
        self.page = page
        self.selected_city = None
        self.data = []
        logger.info("Initialized HomePage object.")

    def navigate(self):
        """Navigate to the Wander website homepage."""
        logger.info("Navigating to Wander homepage.")
        self.page.goto("https://www.wander.com")
        
    def click_on_wherever_button(self):
        """Click the 'Wherever' button to open location selection."""
        wherever_button = HomePageButtonSelectors.BUTTON_WHEREVER.value
        self.page.get_by_role(wherever_button[0], name=wherever_button[1]).click()
        logger.info("Clicking 'Wherever' button.")
        
    def click_on_whenever_button(self):
        """Click the 'Whenever' button to open date selection."""
        whenever_button = HomePageButtonSelectors.BUTTON_WHENEVER.value
        self.page.get_by_role(whenever_button[0], name=whenever_button[1]).click()
        logger.info("Clicking 'Whenever' button.")
    
    def click_on_whoever_button(self):
        """Click the 'Whoever' button to open guest selection."""
        whoever_button = HomePageButtonSelectors.BUTTON_WHOEVER.value
        self.page.get_by_role(whoever_button[0], name=whoever_button[1]).click()
        logger.info("Clicking 'Whoever' button.")
        
    def click_on_search_button(self):
        """
        Click the search button and wait for results to load.
        Ensures that property listings are visible before proceeding.
        """
        logger.info("Clicking search button.")
        search_button = HomePageButtonSelectors.BUTTON_SEARCH.value
        self.page.locator(search_button[1]).click()
        self.page.wait_for_load_state('networkidle')
        logger.info("Waiting for properties to be displayed.")
        self.page.wait_for_selector('#properties-list a.card-wrapper').is_visible()

    def select_location(self, city: str):
        """
        Select a specific city from the location options.

        Args:
            city (str): The name of the city to select
        """
        logger.info(f"Selecting location: {city}.")
        self.page.wait_for_load_state('networkidle')
        label_name = f"LABEL_{city.replace(' ', '_').upper()}"
        city_selector = HomePageCitySelectors[label_name]
        self.selected_city = city_selector.value
        scroll_to_city(self.page, self.selected_city)
        self.page.get_by_label(city_selector.value).check()
        
    def verify_city_is_selected(self, city):
        """
        Verify that a specific city is selected in the filter.

        Args:
            city (str): The city name to verify
        """
        logger.info(f"Verifying that {city} is selected.")
        self.page.wait_for_load_state('networkidle')
        label_name = f"LABEL_{city.replace(' ', '_').upper()}"
        city_selector = HomePageCitySelectors[label_name]
        expect(self.page.get_by_role("button", name=city_selector.value)).to_be_visible()

    def verify_all_cities_are_correct(self):
        """
        Verify that all displayed properties are in the selected city.
        Checks each property's location text against the selected city.
        """
        logger.info(f"Verifying all properties are in {self.selected_city}.")
        self.page.wait_for_load_state('networkidle')
        city_elements = self.page.locator('div.text-property-eyebrow')
        count = city_elements.count()

        for i in range(count):
            city_name = city_elements.nth(i).inner_text().lower()
            assert self.selected_city in city_name, f"Expected city '{self.selected_city}' in '{city_name}'"

    def verify_number_of_properties(self):
        """
        Verify that the number of displayed properties matches the expected count
        from the PropertiesData configuration.
        """
        logger.info("Verifying the number of displayed properties.")
        self.page.wait_for_load_state('networkidle')
        properties_data = PropertiesData[self.selected_city.replace(' ', '_').upper()].value
        self.page.wait_for_selector('div.text-property-eyebrow',timeout=3000).is_visible()
        city_elements = self.page.locator('div.text-property-eyebrow')
        count = city_elements.count()
        assert(count == properties_data["PROPERTIES"] + properties_data["COMMINGSOON"])
        
    def verify_cities_are_selected(self, city_one, city_two):
        """
        Verify that two cities are selected in the filter.

        Args:
            city_one (str): First city name to verify
            city_two (str): Second city name to verify
        """
        logger.info(f"Verifying that {city_one} and {city_two} are selected.")
        self.page.wait_for_load_state('networkidle')
        self.data.append(city_one)
        self.data.append(city_two)
        expect(self.page.get_by_role("button", name=f"{city_two.lower()}, {city_one.lower()}")).to_be_visible()

    def verify_all_the_cities_are_correct(self): 
        """
        Verify that all displayed properties are in either of the two selected cities.
        Checks each property's location against both selected cities.
        """
        logger.info("Verifying that all properties are in the selected cities.")
        scroll_to_bottom(self.page)
        self.page.wait_for_load_state('networkidle')  
        self.page.wait_for_selector('div.text-property-eyebrow',timeout=3000).is_visible()
        city_elements = self.page.locator('div.text-property-eyebrow')
        count = city_elements.count() 
        for i in range(count):
            city_name = city_elements.nth(i).inner_text().lower() 
            logger.debug(f"Property {i+1}: {city_name}")
            assert self.data[0].lower() in city_name or self.data[1].lower() in city_name, \
                f"City name '{city_name}' does not match expected values: {self.data[0]}, {self.data[1]}"
        
    def select_dates(self, date_one, date_two):
        """
        Select check-in and check-out dates.

        Args:
            date_one (str): Check-in date to select
            date_two (str): Check-out date to select
        """
        logger.info(f"Selecting dates: {date_one} to {date_two}.")
        self.page.wait_for_load_state('networkidle')
        self.data.append(date_one)
        self.data.append(date_two)
        self.page.get_by_role("button", name=date_one).first.click()
        self.page.get_by_role("button", name=date_two).first.click()
        
    def verify_filter_date_is_correct(self):
        """
        Verify that the selected dates in the filter match the expected format and values.
        Calculates expected month based on current date and selected dates.
        """
        logger.info("Verifying the selected date range in the filter.")
        self.page.wait_for_load_state('networkidle')
        now = datetime.now()
        current_day = now.day
        start_date = int(self.data[0])-1  
        end_date = int(self.data[1])-1
        if start_date < current_day:
            expected_month = (now.month % 12) + 1 
        else:
            expected_month = now.month
        expected_month_name = (now.replace(month=expected_month)).strftime("%b")
        expected_dates = f"{expected_month_name} {str(start_date)} - {expected_month_name} {str(end_date)}"
        expect(self.page.get_by_role("button", name=expected_dates)).to_be_visible()
        
    def verify_correct_date_of_the_results(self):
        """
        Verify that all property availabilities fall within the selected date range.
        Checks both start and end dates for each property.
        """
        logger.info("Verifying that all results match the selected date range.")
        self.page.wait_for_load_state('networkidle')
        dates_elements = self.page.query_selector_all('span.whitespace-nowrap.text-6-white')
        start_day = int(self.data[0])
        end_day = int(self.data[1])
        for date_element in dates_elements:
            date_text = date_element.inner_text()
            date_parts = date_text.split(' to ')
            result_start_day = int(date_parts[0].split(' ')[1])
            result_end_day = int(date_parts[1].split(' ')[1])
            assert start_day <= result_start_day <= end_day, \
                f"Start date {result_start_day} is outside range {start_day}-{end_day}"
            assert start_day <= result_end_day <= end_day, \
                f"End date {result_end_day} is outside range {start_day}-{end_day}"
            
    def click_on_plus_button_in_whoever(self, quantity):
        """
        Click the plus button to increase guest count.

        Args:
            quantity (str): Number of times to click the plus button
        """
        logger.info("Clicking on plus button to increase guests")
        self.page.wait_for_load_state('networkidle')
        self.data.append(quantity)
        for i in range(int(quantity)):
            self.page.locator("button:has(svg use[href*='plus'])").click()
    
    def verify_amount_of_guests_selected(self, guests):
        """
        Verify that the guest count in the filter matches the expected value.

        Args:
            guests (str): Expected number of guests
        """
        logger.info("Verifying that amount of guests in the button")
        self.page.wait_for_load_state('networkidle')
        expect(self.page.locator(f'button span:has-text("{guests} people")')).to_be_visible()
   
    def verify_guests_number(self):
        """
        Verify that all properties can accommodate the selected number of guests.
        Checks the maximum guest capacity of each property against the selected guest count.
        """
        logger.info("Verifying the amount of guests in the properties")
        expected_guests = int(self.data[0])
        self.page.wait_for_load_state('networkidle')
        self.page.wait_for_selector('#properties-list a').is_visible()
        properties = self.page.query_selector_all('#properties-list a')
        for property in properties:
            guests_locator = property.query_selector("div.flex.items-center.gap-1.text-sm.pl-1 span:nth-of-type(3)")
            guests_text = guests_locator.inner_text() if guests_locator else str(expected_guests + 1)
            guests = int(guests_text.strip())
            assert guests >= expected_guests, f"Expected at least {expected_guests} guests, but found {guests}."
            