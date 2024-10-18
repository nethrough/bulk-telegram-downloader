# 📽️ **Telegram BULK VIDEO Downloader** 


## Overview

Welcome to the **Telegram BULK VIDEO Downloader** repository! This project contains Python scripts that utilize the **Telethon** library to interact with the Telegram API, enabling you to search for Telegram groups and download videos from them seamlessly.

### ✨ Features

- **🔍 Search for Groups:** Find Telegram groups by name and retrieve their unique IDs.
- **📥 Download Media:** Download all video files from a specified Telegram group.
- **⏳ Progress Tracking:** Visualize the download progress for each video file.
- **📦 Zip Files:** Compress downloaded videos into a zip file for easy storage.

---

## Requirements

### 🛠️ **Before You Begin**

Ensure you have the following installed:

- **Python:** Version 3.7 or higher
- **Libraries:** Telethon, tqdm

## Installation

### 🛠️ **Step 1: Clone the Repository**

```bash
git clone https://github.com/yourusername/telegram-media-downloader.git
cd telegram-media-downloader
```

### 🛠️ **Step 2: Install Required Libraries**

Install the necessary libraries using pip:

```bash
pip install telethon tqdm
```

## Configuration

### ⚙️ **Step 3: Configure Your Settings**

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

### 🏃‍♂️ **Step 4: Run the Scripts**

1. **Search for a Group:**

   To search for a Telegram group by its name, run the following command:

   ```bash
   python search_group.py  # Replace with the actual filename of your search script
   ```

   - **Output:** If the group is found, the script will display the group's ID.

2. **Download Videos:**

   To download all video files from a specified Telegram group, execute the following command:

   ```bash
   python download_videos.py  # Replace with the actual filename of your download script
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

- [Telethon](https://docs.telethon.dev/) - The library used to interact with the Telegram API.
- [tqdm](https://tqdm.github.io/) - For progress bar functionality.

---

## 🌟 **Happy Coding!** 🌟
