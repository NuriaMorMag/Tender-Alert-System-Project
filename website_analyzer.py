import requests

# Analyze a company website
def analyze_website(url):
    try:
        # Fetch website content
        response = requests.get(url)

        # Return first 500 characters
        return response.text[:500]

    except:
        # If something fails, return empty string
        return ""