import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """Extracts filename from URL or generates a unique one if missing."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    if not filename:  # If no filename found, generate one
        filename = f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"
    return filename

def file_already_exists(filepath, content):
    """Check if a file with the same content already exists to avoid duplicates."""
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            existing_content = f.read()
        return existing_content == content
    return False

def fetch_image(url):
    """Fetch and save image from the given URL with error handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for HTTP issues

        # Check if response is actually an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipping: {url} (Not an image, Content-Type: {content_type})")
            return

        # Ensures directory exists
        os.makedirs("Fetched_Images", exist_ok=True)

        # Determines filename
        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)

        # Prevents duplicate downloads
        if file_already_exists(filepath, response.content):
            print(f"✓ Duplicate detected: {filename} (Already exists)")
            return

        # Saves image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error while fetching {url}: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask user for single or multiple URLs
    urls = input("Please enter image URL(s) (separate multiple URLs with spaces): ").split()

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
