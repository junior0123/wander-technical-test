
# Technical Test 🔍

## Introduction

This repository showcases a framework for web automation utilizing **Playwright** and **Cucumber**. It features integrated loggers and reports to enhance test visibility and management. Explore the project to understand how automated tests are structured and executed effectively.

## Prerequisites

Before you begin, ensure you have **Python** and **pip** installed on your system. You can verify your installations by running the following commands in your terminal:

```bash
python --version
pip --version
```

If Python is not installed, you can download it from [python.org](https://www.python.org/downloads/). Pip is generally installed automatically with Python.

## Setting Up the Virtual Environment 🛠️

1. **Clone the repository:**

   ```bash
   git clone git@github.com:junior0123/wander-technical-test.git
   cd wander-technical-test
   ```

2. **Create a virtual environment:**

   In your terminal, navigate to the project directory and run:

   ```bash
   python -m venv env
   ```

   This command creates a new virtual environment named `env` in your current directory.

3. **Activate the virtual environment:**

   - On **Windows**:

     ```bash
     env\Scripts\activate
     ```

   - On **macOS** and **Linux**:

     ```bash
     source env/bin/activate
     ```

   Activating the virtual environment ensures that the installed libraries and Python commands run within this isolated environment.

## Installing Dependencies 📦

1. **Install project dependencies:**

   Once the virtual environment is activated, install the required libraries using pip:

   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## Running the Project 🚀

To run the project and initiate the automated job search with integrated AI, follow these steps:

1. **Run the main script:**

   ```bash
   pytest
   ```

   This command will start the job search process, where the AI analyzes job descriptions and compares the requirements with the user profile defined in the code.

2. **Running Tests by Marker:**

   You can also execute tests based on specific markers. Here are some examples:

   - **Location Filter Tests:**  
     ```bash
     pytest -m filter_location
     ```

   - **Date Filter Tests:**  
     ```bash
     pytest -m filter_dates
     ```

   - **Guest Filter Tests:**  
     ```bash
     pytest -m filter_guests
     ```

   - **Test Case Specific Markers:**
     - **TC-01:** Verify city selection and property listing functionality  
       ```bash
       pytest -m TC-01
       ```
     - **TC-02:** Verify multiple cities selection and filtering  
       ```bash
       pytest -m TC-02
       ```
     - **TC-03:** Validate date range selection and availability  
       ```bash
       pytest -m TC-03
       ```
     - **TC-04:** Verify guest count filter and property capacity  
       ```bash
       pytest -m TC-04
       ```

3. **Additional Configuration:**

   To ensure strict marker validation and generate HTML reports, include the following in your configuration file:

   ```ini
   addopts = --strict-markers --html=reports/report.html
   ```

4. **Viewing Results:**

   Results can be viewed in the generated report located in the `/reports` folder. Open `report.html` to access detailed test outcomes. If any issues arise, check the logs in the `/log` directory.

5. **Configuring Execution:**

   You can modify execution parameters in the `/config/config.yaml` file:

   ```yaml
   default:
     base_url: "https://wander.com"  # Base URL for the tests
     browser: "chromium"               # Default browser: chromium, firefox, webkit
     headless: False                    # Run in headless mode (no UI)
     timeout: 10                        # Max wait time for actions (in seconds)
     slow_mo: 250                       # Delay actions to simulate human interaction (in milliseconds)
     retries: 2                         # Number of retries for a failed test
   ```

   You can also add additional tests in the `features` directory for execution.

## About the Author 👨‍💻

This project was created by **Alvaro Sivila**, a dedicated QA Automation Engineer with expertise in various automation tools and frameworks. If you're interested in my work, feel free to check out my portfolio or connect with me on LinkedIn:

- **Portfolio:** [Portfolio](https://junior0123.github.io/QAPortfolio/)
- **LinkedIn:** [Alvaro Sivila](https://www.linkedin.com/in/alvaro-sivila-ram%C3%ADrez-0a8537113/)

---
