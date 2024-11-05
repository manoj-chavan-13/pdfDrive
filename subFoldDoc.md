# Documentation for `subFold.py`

## Overview
The `subFold.py` script enables users to authenticate with Google Drive and download all PDF files from a specified parent folder, including any PDFs found in its subfolders. This documentation will provide a comprehensive explanation of the code, including its functionality and purpose.

## Code Explanation

```python
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
```
- **Imports**: The script starts by importing necessary classes from the `PyDrive` library:
  - `GoogleAuth`: Manages the authentication process with Google Drive.
  - `GoogleDrive`: Represents the Google Drive API interface for file operations.
  - `os`: A standard Python library that allows interaction with the operating system, although it's not utilized directly in this script.

```python
# Authenticate with Google Drive
gauth = GoogleAuth()
```
- **Authentication Object**: An instance of `GoogleAuth` is created. This object is responsible for managing the authentication process with Google Drive.

```python
# Load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
```
- **Load Credentials**: The script attempts to load saved user credentials from a file named `mycreds.txt`. If valid credentials exist, they will be used for authentication.

```python
if gauth.credentials is None:
    # Authenticate if credentials are not available
    gauth.LocalWebserverAuth()  # Creates a local webserver for authentication
    gauth.SaveCredentialsFile("mycreds.txt")
```
- **Check Credentials**:
  - This `if` statement checks if credentials have been loaded. If `gauth.credentials` is `None`, it indicates that no credentials are available and the user needs to authenticate.
  - `gauth.LocalWebserverAuth()`: This method starts the authentication process by creating a local web server. The user will be prompted to log in to their Google account and authorize access to the application.
  - Upon successful authentication, the credentials are saved in `mycreds.txt` for future use.

```python
elif gauth.access_token_expired:
    # Refresh the credentials if they have expired
    gauth.Refresh()
    gauth.SaveCredentialsFile("mycreds.txt")
```
- **Refresh Credentials**:
  - This `elif` block checks if the access token has expired. If it has, the credentials are refreshed using `gauth.Refresh()`.
  - The refreshed credentials are saved back to `mycreds.txt`.

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
- **Create Drive Instance**: A `GoogleDrive` instance is created using the authenticated `gauth` object. This instance will be utilized to interact with Google Drive, such as listing and downloading files.

```python
# Replace 'your-parent-folder-id' with the actual ID of the parent folder
parent_folder_id = 'your-parent-folder-id'
```
- **Parent Folder ID**: The `parent_folder_id` variable should be replaced with the actual ID of the Google Drive folder from which you want to download PDF files. This ID can be found in the URL of the folder when viewed in Google Drive.

```python
def download_pdfs_from_folder(folder_id):
```
- **Function Definition**: This line defines a function named `download_pdfs_from_folder`, which takes a `folder_id` as an argument. This function will be responsible for downloading all PDF files from the specified folder and any of its subfolders.

```python
    # List all files and folders in the current folder
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
```
- **List Files and Folders**:
  - This line retrieves all files and folders in the specified folder (`folder_id`). It uses a query to filter out any items that have been deleted (trashed).
  - The results are stored in the `file_list` variable, which contains a list of file objects.

```python
    for file in file_list:
```
- **Iterate Over Files**: This line starts a `for` loop to iterate through each file object in `file_list`.

```python
        if file['mimeType'] == 'application/pdf':
            # Download the PDF file
            print(f'Downloading {file["title"]}...')
            file.GetContentFile(file['title'])
```
- **Download PDF Files**:
  - The `if` statement checks if the current file's MIME type is `application/pdf`. If it is, the script proceeds to download it.
  - It prints a message indicating the file's title and that it is being downloaded.
  - `file.GetContentFile(file['title'])`: This method downloads the PDF file and saves it in the current working directory with its original title.

```python
        elif file['mimeType'] == 'application/vnd.google-apps.folder':
            # If the file is a folder, call the function recursively
            print(f'Entering folder: {file["title"]}')
            download_pdfs_from_folder(file['id'])
```
- **Handle Subfolders**:
  - The `elif` statement checks if the current file is a folder (MIME type `application/vnd.google-apps.folder`).
  - If it is a folder, the script prints a message indicating that it is entering the folder and recursively calls the `download_pdfs_from_folder` function, passing the ID of the subfolder.

```python
# Start the recursive download from the parent folder
download_pdfs_from_folder(parent_folder_id)
```
- **Initiate Download**: This line calls the `download_pdfs_from_folder` function with the `parent_folder_id`, starting the recursive download process from the specified parent folder.

```python
print("All PDFs have been downloaded successfully!")
```
- **Completion Message**: After all files have been processed and downloaded, this line prints a message indicating that the process has been completed successfully.

## Conclusion
The `subFold.py` script effectively downloads all PDF files from a specified Google Drive folder and its subfolders by handling authentication and utilizing the Google Drive API to recursively retrieve and download files.

### Usage Instructions
1. Ensure you have installed the required libraries, particularly `PyDrive`.
2. Replace `'your-parent-folder-id'` in the code with the actual ID of the parent folder from which you wish to download PDFs.
3. Run the script using Python from your command line or terminal.

For additional information and detailed explanation of the code, please refer to the **Code Explanation** section in this document.
