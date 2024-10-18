from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaDocument
import os
import zipfile
from tqdm import tqdm

# Your API credentials (replace the placeholders with your actual credentials)
api_id = 'YOUR_API_ID'  # Your API ID
api_hash = 'YOUR_API_HASH'  # Your API Hashs
phone = 'YOUR_PHONE_NUMBER'  # Your phone number

# Directory to save media (replace with your own directory path)
download_directory = 'YOUR_DOWNLOAD_DIRECTORY_PATH'  # Example: r'C:\Users\YourName\Downloads'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

async def download_telegram_group(group_id):
    async with client:
        # Connect to the group using its ID
        group = await client.get_entity(group_id)

        # Create a set to track downloaded message IDs
        downloaded_message_ids = set()

        # Get all messages from the group
        async for message in client.iter_messages(group):
            if message.id in downloaded_message_ids:
                continue  # Skip already downloaded messages

            if message.media and isinstance(message.media, MessageMediaDocument):
                # Check if the media is a video based on its MIME type
                if message.media.document.mime_type.startswith('video/'):
                    file_name = next((attr.file_name for attr in message.media.document.attributes if hasattr(attr, 'file_name')), f'video_{message.id}.mp4')
                    file_path = os.path.join(download_directory, file_name)

                    # Skip downloading if the file already exists
                    if os.path.exists(file_path):
                        print(f'Skipping {file_name}, already downloaded.')
                        continue

                    # Get the total size of the video file
                    total_size = message.media.document.size if hasattr(message.media.document, 'size') and message.media.document.size else 1

                    # Download media with progress
                    with tqdm(total=total_size, unit='B', unit_scale=True, desc=f'Downloading {os.path.basename(file_path)}', bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
                        # Define the progress callback
                        async def progress_callback(current, total):
                            pbar.n = current
                            pbar.total = total
                            pbar.refresh()

                        await message.download_media(file=file_path, progress_callback=progress_callback)

            # Mark this message as downloaded
            downloaded_message_ids.add(message.id)

def zip_downloaded_files():
    # Create a zip file (replace with your own zip file path)
    zip_file_path = 'YOUR_ZIP_FILE_PATH'  # Example: r'C:\Users\YourName\telegram_downloads.zip'
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        # Walk through the download directory
        for root, dirs, files in os.walk(download_directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, download_directory))

# Replace with the actual group ID
group_id = 'YOUR_GROUP_ID'  # Use your group ID here

# Run the download and then zip the files
with client:
    client.loop.run_until_complete(download_telegram_group(group_id))

# Zip the downloaded files
zip_downloaded_files()
print('All files have been zipped successfully!')
