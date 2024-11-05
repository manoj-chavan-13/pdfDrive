from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Authenticate with Google Drive
gauth = GoogleAuth()

# Load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
    # Authenticate if credentials are not available
    gauth.LocalWebserverAuth()  # Creates a local webserver for authentication
    gauth.SaveCredentialsFile("mycreds.txt")
elif gauth.access_token_expired:
    # Refresh the credentials if they have expired
    gauth.Refresh()
    gauth.SaveCredentialsFile("mycreds.txt")
else:
    # Authorize with the saved credentials
    gauth.Authorize()

# Create a Google Drive instance
drive = GoogleDrive(gauth)

# Replace 'your-parent-folder-id' with the actual ID of the parent folder
parent_folder_id = 'your-parent-folder-id'

def download_pdfs_from_folder(folder_id):
    # List all files and folders in the current folder
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    
    for file in file_list:
        if file['mimeType'] == 'application/pdf':
            # Download the PDF file
            print(f'Downloading {file["title"]}...')
            file.GetContentFile(file['title'])
        elif file['mimeType'] == 'application/vnd.google-apps.folder':
            # If the file is a folder, call the function recursively
            print(f'Entering folder: {file["title"]}')
            download_pdfs_from_folder(file['id'])

# Start the recursive download from the parent folder
download_pdfs_from_folder(parent_folder_id)

print("All PDFs have been downloaded successfully!")
