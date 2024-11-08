


# Automated Product Finder with Selenium
### Introduction:

Tired of scrolling through multiple pages to find products that meet your criteria? This tool automates the process of gathering information such as product prices, ratings, and more, from e-commerce websites like Amazon, making your search efficient and effortless!

### Features:
Automatic Web Scraping: Using Selenium and BeautifulSoup to gather product details.
Supports Chrome Version 125: Compatible with Chrome 125, ensuring smooth functionality.
Customizable: Tailor the search criteria for different products and stores.
Prerequisites:
Before running the script, make sure you have the following:

Google Chrome Browser (Version 125): You can check your Chrome version by navigating to the three vertical dots (top right corner), selecting "Help," and then "About Google Chrome."

Chrome Web Driver: Download the appropriate driver for your version of Chrome.

Download Chrome WebDriver for Chrome 125
### Python Libraries:

`Selenium`
`BeautifulSoup`
`Unidecode`
`Time`
`OS`
You can install the required Python libraries using pip:


pip install selenium beautifulsoup4 unidecode


### Setup Instructions:
Download Chrome Web Driver:

Navigate to the provided link and download the chromedriver-win64.zip file.
Extract the contents of the zip file and place chromedriver.exe in a folder on your computer.
Download the Python Script:

Clone this repository or download the Python script.
Modify the WebDriver Path:

Update the following line in the Python script with the correct path to your chromedriver.exe:


driver = webdriver.Chrome(executable_path=r"C:\Path\To\chromedriver.exe", options= webdriver.ChromeOptions())
Run the Script:

Execute the script to start gathering product information from e-commerce sites.
How It Works:
The script automates the browsing process using the following flow:

It initializes a Selenium WebDriver (Chrome) and navigates to an e-commerce website.
The script searches for products, scrapes relevant information (price, ratings, etc.), and stores it for analysis.
You can customize the search criteria (XPATH) to refine the results.
