import requests

# Get text content from a website
def get_website_text(url):
    try:
        response = requests.get(url)
        return response.text  # Return full HTML text
    except:
        return ""  # Return empty if error