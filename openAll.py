import webbrowser

def open_urls_in_chrome(file_path):
    # Path to the Chrome executable
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    
    try:
        # Open the file containing URLs
        with open(file_path, 'r') as file:
            urls = file.readlines()
            
        # Strip any whitespace characters like `\n` at the end of each line
        urls = [url.strip() for url in urls if url.strip()]
        
        # Open each URL in a new tab
        for url in urls:
            webbrowser.get(chrome_path).open_new_tab(url)
    
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'urls.txt' with the path to your file
open_urls_in_chrome('urls.txt')
