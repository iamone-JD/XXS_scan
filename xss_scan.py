import requests
import urllib.parse
import argparse
import json

def text_xss(url, cookies_arg):
    payload = '<script>alert("XSS")</script>'
    try:
        # Check if the URL is valid
        result = urllib.parse.urlparse(url)
        if not all([result.scheme, result.netloc]):
            raise ValueError("Invalid URL")

        parsed_cookies = None
        if cookies_arg:
            try:
                # Try to parse as JSON string
                parsed_cookies = json.loads(cookies_arg)
            except json.JSONDecodeError:
                # If JSON parsing fails, try to read as a file path
                try:
                    with open(cookies_arg, 'r') as f:
                        parsed_cookies = json.load(f)
                except FileNotFoundError:
                    print(f"Error: Cookie file not found at {cookies_arg}")
                    # Proceed without cookies if file not found or parsing error
                    parsed_cookies = None
                except json.JSONDecodeError:
                    print(f"Error: Could not parse JSON from file {cookies_arg}")
                    parsed_cookies = None
                except Exception as e:
                    print(f"Error processing cookie file {cookies_arg}: {e}")
                    parsed_cookies = None
            except Exception as e:
                print(f"Error processing cookies argument: {e}")
                parsed_cookies = None

        # Send the request
        if parsed_cookies:
            response = requests.get(str(url) + str(payload), cookies=parsed_cookies, timeout=5)
        else:
            response = requests.get(str(url) + str(payload), timeout=5)
        
        response.raise_for_status()  # Raise an exception for HTTP errors
        # Check if the payload is reflected in the response
        if payload in response.text:
            print(f"Vulnerable to XSS at {url}")
        else:
            print(f"Not vulnerable to XSS at {url}")
            # print(response.text) # Optional: print response text if not vulnerable
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
    parser.add_argument('--cookies', help='Cookies to use for the request, as a JSON string (e.g., \'{"name": "value"}\') or path to a JSON file containing cookies.', required=False)
    args = parser.parse_args()
    text_xss(args.url, args.cookies)
