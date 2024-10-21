import yaml
from playwright.sync_api import sync_playwright

def load_config():
    """
    Loads the browser configuration from a YAML file.

    This function opens the 'config.yaml' file and safely loads the configuration 
    data, returning it as a dictionary.
    
    Returns:
        dict: The loaded configuration data from the YAML file.
    """
    with open('config/config.yaml', 'r') as config_file:
        return yaml.safe_load(config_file)

class BrowserManager:
    """
    Manages browser instances using Playwright.

    The `BrowserManager` class handles the creation and management of browser instances 
    based on a configuration file. It supports launching different browsers (Chromium, Firefox, WebKit) 
    in either headless or non-headless mode, with customizable timeouts and slow-motion settings.
    """
    
    def __init__(self):
        """
        Initializes the BrowserManager by loading the configuration and starting Playwright.

        It reads the default configuration values from the YAML file, sets the browser type, 
        headless mode, timeout, and slow-motion settings, and then launches the browser.
        """
        self.playwright = sync_playwright().start()
        config = load_config()['default']
        self.browser_type = config['browser']
        self.headless = config['headless']
        self.timeout = config['timeout']
        self.slow_mo = config['slow_mo']
        self.browser = self._launch_browser()

    def _launch_browser(self):
        """
        Launches the browser based on the configuration.

        It checks the `browser_type` from the config and launches the appropriate browser 
        (Chromium, Firefox, or WebKit). The browser is launched in headless mode if specified 
        and with optional slow-motion delays.
        
        Returns:
            Browser: A Playwright browser instance.

        Raises:
            ValueError: If the browser type specified in the config is unsupported.
        """
        if self.browser_type == 'chromium':
            return self.playwright.chromium.launch(headless=self.headless, slow_mo=self.slow_mo)
        elif self.browser_type == 'firefox':
            return self.playwright.firefox.launch(headless=self.headless, slow_mo=self.slow_mo)
        elif self.browser_type == 'webkit':
            return self.playwright.webkit.launch(headless=self.headless, slow_mo=self.slow_mo)
        else:
            raise ValueError(f"Unsupported browser: {self.browser_type}")

    def new_page(self):
        """
        Creates a new page in the browser.

        This method opens a new tab or page in the currently active browser instance.
        
        Returns:
            Page: A new browser page.
        """
        return self.browser.new_page()

    def new_context(self):
        """
        Creates a new browser context.

        A browser context allows for multiple independent sessions within the same browser. 
        Each context can have its own cookies, cache, and settings.
        
        Returns:
            BrowserContext: A new browser context instance.
        """
        return self.browser.new_context()

    def close(self):
        """
        Closes the browser and stops Playwright.

        This method closes the currently active browser instance and stops the Playwright process 
        to free up resources.
        """
        self.browser.close()
        self.playwright.stop()
