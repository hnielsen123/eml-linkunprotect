import argparse
import os
import re
from urllib.parse import unquote, urlparse, parse_qs


# Function to decode URLs
def decode_url(protected_url):
    parsed_url = urlparse(protected_url)
    query_string = parse_qs(parsed_url.query)
    
    # Error handling for missing 'a' key
    if 'a' in query_string:
        # Double unquoting to handle potential double encoding
        decoded_url = unquote(unquote(query_string['a'][0]))
        return decoded_url
    else:
        print(f"Could not find 'a' key in query string for URL: {protected_url}")
        return None


# Function to remove soft line breaks
def remove_soft_breaks(file_path):
    new_lines = []
    append_next_line = False
    buffer = ""
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.endswith('='):
                buffer += line[:-1]
            else:
                new_line = buffer + line
                new_lines.append(new_line)
                buffer = ""
                
    return '\n'.join(new_lines)


# Argument parsing
parser = argparse.ArgumentParser(description='Process an .eml file to decode URLs.')

parser.add_argument('eml_file', type=str, help='Path to the .eml file you want to process.')

args = parser.parse_args()

eml_file_path = args.eml_file


# Remove soft line breaks (idiosyncracy of MIME used in .eml files)
email_content = remove_soft_breaks(eml_file_path)

encoded_urls = re.findall(r'https://linkprotect.cudasvc[^\s"]+', email_content)
decoded_urls = []


print(encoded_urls)

for url in encoded_urls:
	decoded_url = decode_url(url)[2:]
	decoded_urls.append(decoded_url)

for enc, dec in zip(encoded_urls, decoded_urls):
	email_content = email_content.replace(enc, dec)



# Write the new content to a new .eml file
file_dir, file_name = os.path.split(eml_file_path)
new_file_name = "decoded_" + file_name
new_file_path = os.path.join(file_dir, new_file_name)

with open(new_file_path, 'w') as new_file:
    new_file.write(email_content)


