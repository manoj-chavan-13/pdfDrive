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

# Replace 'your-folder-id' with the actual ID of the folder containing the PDFs
folder_id = 'your-folder-id'

# List and download all PDF files in the folder
file_list = drive.ListFile({'q': f"'{folder_id}' in parents and mimeType='application/pdf'"}).GetList()

for file in file_list:
    print(f'Downloading {file["title"]}...')
    file.GetContentFile(file['title'])  # Saves the file with its original name

print("All PDFs have been downloaded successfully!")
