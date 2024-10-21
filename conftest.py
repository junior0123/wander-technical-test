import pytest
from config.browser_config import BrowserManager
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_manager():
    """
    Initializes the browser for the entire test session.

    This fixture creates a browser for all the tests executed in a session.
    It uses the previously defined `BrowserManager` class to manage the browser instance.
    Yields:
        context: A new browser context that can be used to generate pages.
    After all tests are done, it closes both the context and the browser.
    """
    try:
        browser = BrowserManager()  # We use the class we have already created
        context = browser.new_context()
        yield context  # Provide the browser context to the tests
        context.close()
        browser.close()  # Close the browser after all tests
    except Exception as e:
        print(f"Error: {e}")

@pytest.fixture(scope="function")
def page(browser_manager):
    """
    Provides a new browser page for each test.

    This fixture generates a new browser page before each test and closes it after execution.
    
    Args:
        browser_manager: The browser context provided by the `browser_manager` fixture.
    
    Yields:
        page: A new browser page to be used in the test.
    
    After the test, the page is automatically closed.
    """
    try:
        page = browser_manager.new_page()
        yield page  # Provide the page to the functions that need it
        page.close()  # Close the page after each test
    except Exception as e:
        print(f"Error: {e}")
