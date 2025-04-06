import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def clone_website(url, output_dir="cloned_site"):
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Validate URL
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Fetch the webpage
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch URL: {e}")
        return

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all resources (CSS, JS, images)
    resources = []
    tags = {'link': 'href', 'script': 'src', 'img': 'src'}
    
    for tag in tags:
        for resource in soup.find_all(tag):
            resource_url = resource.get(tags[tag])
            if resource_url:
                resources.append(resource_url)

    # Download resources
    downloaded_files = {}
    for resource_url in resources:
        # Handle relative URLs
        full_url = urljoin(url, resource_url)
        
        # Get file path
        path = urlparse(full_url).path
        filename = os.path.basename(path)
        
        if not filename:
            filename = "index.html"
        
        local_path = os.path.join(output_dir, filename)
        
        # Download file
        try:
            resource_response = requests.get(full_url)
            resource_response.raise_for_status()
            with open(local_path, 'wb') as f:
                f.write(resource_response.content)
            downloaded_files[resource_url] = filename
        except Exception as e:
            print(f"Failed to download {full_url}: {e}")

    # Update HTML with local paths
    for tag in tags:
        for resource in soup.find_all(tag):
            resource_url = resource.get(tags[tag])
            if resource_url in downloaded_files:
                resource[tags[tag]] = downloaded_files[resource_url]

    # Save main HTML file
    main_page = os.path.join(output_dir, "index.html")
    with open(main_page, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))

    print(f"Website cloned to {output_dir}")

# Usage
clone_website("https://example.com")

#
#
#
# =======================================================
#
#
#
#
import os
import requests
from urllib.parse import urlparse, urljoin
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup

def download_file(url, output_dir="."):
    """Download a file from a URL and save it to the output directory."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "index.html"

        # Save file
        file_path = os.path.join(output_dir, filename)
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {file_path}")
        return file_path
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

def can_fetch(url, user_agent="*"):
    """Check if the URL can be fetched based on robots.txt rules."""
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        return rp.can_fetch(user_agent, url)
    except Exception as e:
        print(f"Failed to read robots.txt for {url}: {e}")
        return True  # Assume fetching is allowed if robots.txt is unavailable

def recursive_download(url, output_dir=".", user_agent="*", depth=1):
    """Recursively download files from a URL."""
    if depth < 0:
        return

    if not can_fetch(url, user_agent):
        print(f"Skipping {url} (disallowed by robots.txt)")
        return

    # Download the main file
    downloaded_file = download_file(url, output_dir)
    if not downloaded_file:
        return

    # If the file is HTML, parse it for links
    if downloaded_file.endswith(".html"):
        with open(downloaded_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            for link in soup.find_all('a', href=True):
                next_url = urljoin(url, link['href'])
                recursive_download(next_url, output_dir, user_agent, depth - 1)

def main():
    import argparse

    parser = argparse.ArgumentParser(description="A Python implementation of wget.")
    parser.add_argument("url", help="URL to download")
    parser.add_argument("-o", "--output", default=".", help="Output directory")
    parser.add_argument("-r", "--recursive", action="store_true", help="Enable recursive download")
    parser.add_argument("-d", "--depth", type=int, default=1, help="Recursion depth (default: 1)")
    parser.add_argument("-U", "--user-agent", default="*", help="User agent for robots.txt checking")
    args = parser.parse_args()

    if args.recursive:
        recursive_download(args.url, args.output, args.user_agent, args.depth)
    else:
        download_file(args.url, args.output)

if __name__ == "__main__":
    main()

