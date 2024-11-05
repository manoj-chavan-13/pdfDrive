# Documentation for `inFolder.py`

## Overview
The `inFolder.py` script is designed to authenticate with Google Drive and download all PDF files from a specific folder identified by its folder ID. This documentation will provide a detailed explanation of the code, including its functionality and purpose.

## Code Explanation

```python
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
```
- **Imports**: The script begins by importing necessary classes from the `PyDrive` library:
  - `GoogleAuth`: Handles the authentication process for Google Drive.
  - `GoogleDrive`: Represents the Google Drive API interface for file operations.
  - `os`: A standard Python library that provides functions to interact with the operating system (though it’s not directly used in this script).

```python
# Authenticate with Google Drive
gauth = GoogleAuth()
```
- **Authentication Object**: An instance of `GoogleAuth` is created. This object will manage the authentication process with Google Drive.

```python
# Load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
```
- **Load Credentials**: This line attempts to load saved user credentials from a file named `mycreds.txt`. If the credentials are valid, they will be used for authentication.

```python
if gauth.credentials is None:
    # Authenticate if credentials are not available
    gauth.LocalWebserverAuth()  # Creates a local webserver for authentication
    gauth.SaveCredentialsFile("mycreds.txt")
```
- **Check Credentials**:
  - This `if` statement checks if the credentials have been loaded. If `gauth.credentials` is `None`, it means that no credentials are available (the user needs to authenticate).
  - `gauth.LocalWebserverAuth()`: This method initiates the authentication process by creating a local web server. The user is prompted to log in to their Google account and grant access to the application.
  - After successful authentication, the credentials are saved in `mycreds.txt` for future use.

```python
elif gauth.access_token_expired:
    # Refresh the credentials if they have expired
    gauth.Refresh()
    gauth.SaveCredentialsFile("mycreds.txt")
```
- **Refresh Credentials**:
  - This `elif` block checks if the access token has expired. If it has, the credentials are refreshed using `gauth.Refresh()`.
  - The refreshed credentials are then saved back to `mycreds.txt`.

```python
else:
    # Authorize with the saved credentials
    gauth.Authorize()
```
- **Authorize Existing Credentials**: If valid credentials are available and not expired, this line authorizes the application to use those credentials.

```python
# Create a Google Drive instance
drive = GoogleDrive(gauth)
```
- **Create Drive Instance**: A `GoogleDrive` instance is created using the authenticated `gauth` object. This instance will be used to interact with Google Drive, such as listing and downloading files.

```python
# Replace 'your-folder-id' with the actual ID of the folder containing the PDFs
folder_id = 'your-folder-id'
```
- **Folder ID**: The `folder_id` variable should be replaced with the actual ID of the Google Drive folder from which you want to download PDF files. This ID can be found in the URL of the folder when viewed in Google Drive.

```python
# List and download all PDF files in the folder
file_list = drive.ListFile({'q': f"'{folder_id}' in parents and mimeType='application/pdf'"}).GetList()
```
- **List PDF Files**:
  - This line lists all files in the specified folder (`folder_id`) that have a MIME type of `application/pdf`. 
  - The query uses the Google Drive API’s search capabilities, specifying that it wants files whose parent is the specified folder and whose MIME type is PDF.
  - The result is stored in the `file_list` variable, which contains a list of file objects.

```python
for file in file_list:
    print(f'Downloading {file["title"]}...')
    file.GetContentFile(file['title'])  # Saves the file with its original name
```
- **Download PDF Files**:
  - This `for` loop iterates over each file object in `file_list`.
  - For each file, it prints a message indicating the file's title and that it is being downloaded.
  - `file.GetContentFile(file['title'])`: This method downloads the file and saves it in the current working directory using its original title.

```python
print("All PDFs have been downloaded successfully!")
```
- **Completion Message**: After all files have been downloaded, this line prints a message indicating that the process has completed successfully.

## Conclusion
The `inFolder.py` script efficiently downloads all PDF files from a specified Google Drive folder by handling authentication and using the Google Drive API to retrieve and download files. 

### Usage Instructions
1. Ensure that you have installed the required libraries, especially `PyDrive`.
2. Replace `'your-folder-id'` in the code with the actual folder ID from which you want to download PDFs.
3. Run the script using Python in your command line or terminal.

For additional information and detailed explanation of the code, please refer to the **Code Explanation** section in this document.
