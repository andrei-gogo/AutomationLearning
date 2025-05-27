import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load your CSV
df = pd.read_csv("D:\\10k.csv")

# Function to fetch title
def fetch_title(domain):
    for scheme in ["https://", "http://"]:
        try:
            url = scheme + domain
            response = requests.get(url, timeout=1)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                title_tag = soup.find('title')
                return title_tag.text.strip() if title_tag else "No title found"
        except requests.RequestException:
            continue
    return "Unreachable"

# Apply title fetching
df['Domain Title'] = df['Domain'].apply(fetch_title)

# Save to a new file
df.to_csv("D:\\websites_with_titles.csv", index=False)