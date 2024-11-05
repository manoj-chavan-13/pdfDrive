# Google Drive PDF Downloader

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Getting Started](#getting-started)
   - [Cloning the Repository](#cloning-the-repository)
   - [Setting Up Google Drive API](#setting-up-google-drive-api)
5. [Usage Instructions](#usage-instructions)
   - [Downloading PDFs from a Single Folder](#downloading-pdfs-from-a-single-folder)
   - [Downloading PDFs from Multiple Subfolders](#downloading-pdfs-from-multiple-subfolders)
6. [Code Explanation](#code-explanation)
   - [inFolder.py Documentation](#inFolderpy-documentation)
   - [subFold.py Documentation](#subFoldpy-documentation)
7. [Conclusion](#conclusion)

## Overview
The **Google Drive PDF Downloader** is a Python utility designed to facilitate the download of PDF files stored in Google Drive. This project includes two scripts:
- **`inFolder.py`**: Downloads all PDF files from a specified folder.
- **`subFold.py`**: Downloads PDF files from a parent folder containing multiple subfolders.

## Prerequisites
Before you begin, ensure you have the following:
- **Python 3.x**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Pip**: Python package manager should be installed to manage dependencies.
- **Google Drive API Access**: You will need access to the Google Drive API to authenticate and download files.

## Installation
1. **Install Required Libraries**: Open your command line or terminal and run the following command to install the necessary libraries:
   ```bash
   pip install PyDrive
   ```

## Getting Started

### Cloning the Repository
To download the project files, clone the repository from GitHub. Open your terminal and execute:
```bash
git clone https://github.com/manoj-chavan-13/pdfDrive.git
```
This command creates a directory named `pdfDrive` that contains all the necessary files for the project.

### Setting Up Google Drive API
1. **Google Cloud Console**: Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. **Create a New Project**: Click on "Select a project" and then "New Project".
3. **Enable Google Drive API**: Navigate to **APIs & Services > Library**. Search for **Google Drive API** and enable it.
4. **Create Credentials**: Go to **APIs & Services > Credentials**. Click on "Create Credentials" and select "OAuth client ID".
5. **Configure Consent Screen**: Set up the consent screen as required. 
6. **Download Client Secrets**: After creating credentials, download the `client_secrets.json` file and place it in the same directory as your Python scripts.

## Usage Instructions

### Downloading PDFs from a Single Folder
1. Open the `inFolder.py` script in a text editor.
2. Locate the variable `folder_id` and replace its value with the ID of the Google Drive folder from which you want to download PDFs. The folder ID is part of the URL when you open the folder in Google Drive (e.g., `https://drive.google.com/drive/folders/<folder_id>`).
3. Run the script using:
   ```bash
   python inFolder.py
   ```
4. All PDF files within the specified folder will be downloaded to your current directory.

### Downloading PDFs from Multiple Subfolders
1. Open the `subFold.py` script in a text editor.
2. Find the variable `parent_folder_id` and set its value to the ID of the parent folder containing multiple subfolders.
3. Execute the script with:
   ```bash
   python subFold.py
   ```
4. The script will download all PDF files located in the subfolders, maintaining the original folder structure in your local directory.

## Code Explanation

For a detailed explanation of the code, please check the following documents:
- For **inFolder.py**, see the documentation at `inFolderDoc.md`.
- For **subFold.py**, see the documentation at `subFoldDoc.md`.

These documents provide an in-depth look at the implementation, logic, and functionalities of each script.

## Conclusion
The **Google Drive PDF Downloader** project offers a simple yet effective solution for downloading PDF files from Google Drive. By following the provided steps, users can easily set up their environment, run the scripts, and access their desired PDF documents efficiently. 

Whether you are downloading files from a single folder or multiple subfolders, this tool streamlines the process, saving you time and effort.

For any further questions or support, please refer to the project's GitHub repository or contact the project maintainer directly.

