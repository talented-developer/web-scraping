from urllib.request import urlopen
from bs4 import BeautifulSoup

# Define the target URL to scrape
url = "http://olympus.realpython.org/profiles"

# Open the URL and read the page content
try:
    response = urlopen(url)
    html_content = response.read().decode('utf-8')
except Exception as e:
    print(f"Error fetching the URL: {e}")
    exit(1)  # Exit the program if the URL can't be fetched

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all anchor tags in the parsed HTML
anchor_tags = soup.find_all('a')

# Extract and construct the full URLs from the href attributes
for anchor in anchor_tags:
    # Safely get the href attribute, defaulting to None if not present
    href = anchor.get('href')
    if href:
        # Split the href to get the last part (the profile id)
        profile_id = href.split('/')[-1]  
        # Construct the full URL by appending the profile id to the base URL
        full_profile_url = f"{url}/{profile_id}"
        print(full_profile_url)  # Output the full profile URL

