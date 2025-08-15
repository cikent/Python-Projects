# Web pages are plaintext files formatted as HTML.
# HTML can be parsed with the BeautifulSoup module.
# BeautifulSoup is imported with the name bs4.
# Pass the string with the HTML to the bs4.BeautfiulSoup() function to get a Soup object.
# The Soup object has a select() method that can be passed a string of the CSS selector for an HTML tag.
# You can get a CSS selector string from the browser's developer tools by right-clicking the element and selecting Copy CSS Path.
# The select() method will return a list of matching Element objects.

# Import relelvant modules
import bs4, requests

# Add User Agent Header
headers = {'User-Agent': 'Mozilla/5.0'}

# Create a function() to obtain the Price for the Automate the Boring Stuff with Python book
def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    # Create a Soup Object AND pass the html.parser as the 2nd argument to hide the warning
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Create an Element Selector for Price
    elems = soup.select('#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.aok-offscreen')
    
    # Return the Price Element Text value
    return elems[0].text.strip()
    
# Create a variable for the Price
price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')

# Print to screen the Price value
print('The price is ' + price)