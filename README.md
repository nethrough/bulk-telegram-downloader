# 📽️ **Telegram Media Downloader** 

---

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Telegram Logo" width="150"/>
</div>

## Overview

Welcome to the **Telegram Media Downloader** repository! This project contains Python scripts that utilize the **Telethon** library to interact with the Telegram API, enabling you to search for Telegram groups and download videos from them seamlessly.

### ✨ Features

<ul>
    <li><strong>🔍 Search for Groups:</strong> Find Telegram groups by name and retrieve their unique IDs.</li>
    <li><strong>📥 Download Media:</strong> Download all video files from a specified Telegram group.</li>
    <li><strong>⏳ Progress Tracking:</strong> Visualize the download progress for each video file.</li>
    <li><strong>📦 Zip Files:</strong> Compress downloaded videos into a zip file for easy storage.</li>
</ul>

---

## Requirements

### 🛠️ **Before You Begin**

Ensure you have the following installed:

<ul>
    <li><strong>Python:</strong> Version 3.7 or higher</li>
    <li><strong>Libraries:</strong> Telethon, tqdm</li>
</ul>

## Installation

### 🛠️ **Step 1: Clone the Repository**

```bash
git clone https://github.com/nethrough/bulk-telegram-downloader.git
cd bulk-telegram-downloader
```

### 🛠️ **Step 2: Install Required Libraries**

Install the necessary libraries using pip:

```bash
pip install telethon tqdm
```

## Create Your Telegram App API

### 🛠️ **Step 3: Obtain API Credentials**

1. **Go to the Telegram API Development page:**
   - Visit [my.telegram.org/apps](https://my.telegram.org/apps).
   
2. **Log in with Your Phone Number:**
   - Enter your phone number and verify the code sent to your Telegram app.

3. **Create a New Application:**
   - Click on “Create Application.”
   - Fill in the required fields:
     <ul>
         <li><strong>App Title:</strong> Choose a name for your app.</li>
         <li><strong>Short Name:</strong> A short version of the title.</li>
         <li><strong>URL:</strong> This can be a placeholder (e.g., <code>http://example.com</code>).</li>
     </ul>

4. **Retrieve Your API ID and API Hash:**
   - Once your app is created, you will see your **API ID** and **API Hash**. Keep these confidential as they are essential for authenticating your application.

## Configuration

### ⚙️ **Step 4: Configure Your Settings**

Before running the scripts, modify your API credentials and other parameters in the respective script files. 

- Open the script files and replace the placeholders with your details:

```python
api_id = 'YOUR_API_ID'  # Your API ID from Telegram
api_hash = 'YOUR_API_HASH'  # Your API Hash from Telegram
phone = 'YOUR_PHONE_NUMBER'  # Your phone number including country code
group_name = 'GROUP_NAME_TO_SEARCH'  # The name of the group you want to search for
download_directory = 'YOUR_DOWNLOAD_DIRECTORY_PATH'  # Path to save downloaded media
zip_file_path = 'YOUR_ZIP_FILE_PATH'  # Path to save the zipped file
group_id = 'YOUR_GROUP_ID'  # Use your group ID here
```

## Usage

### 🏃‍♂️ **Step 5: Run the Scripts**

1. **Search for a Group:**

   To search for a Telegram group by its name, run the following command:

   ```bash
   python find_group_id.py  # Replace with the actual filename of your search script
   ```

   - **Output:** If the group is found, the script will display the group's ID.

2. **Download Videos:**

   To download all video files from a specified Telegram group, execute the following command:

   ```bash
   python video_downloader.py  # Replace with the actual filename of your download script
   ```

   - **Progress Tracking:** As videos are downloaded, you will see a progress bar in the console for each file.

3. **Zip Downloaded Files:**

   After downloading, the script will automatically zip the downloaded files for easy storage. A message will confirm when all files have been zipped successfully.

---

## Troubleshooting

### ❗ Common Issues

- **API Credentials Not Working:** Ensure you have copied your API ID and API Hash correctly from the [Telegram API Development page](https://my.telegram.org/apps).
  
- **Group Not Found:** Verify the group name is correct and that you are a member of the group.

- **Permission Errors:** Ensure the specified download directory exists and that you have write permissions.

- **Module Not Found:** If you encounter a `ModuleNotFoundError`, ensure you have installed the required libraries using `pip`.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- <a href="https://docs.telethon.dev/">Telethon</a> - The library used to interact with the Telegram API.
- <a href="https://tqdm.github.io/">tqdm</a> - For progress bar functionality.

---

<div align="center">
    <h3>🌟 Happy Coding! 🌟</h3>
</div>
