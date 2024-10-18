from telethon.sync import TelegramClient

api_id = 'YOUR_API_ID'  # Replace with your API ID
api_hash = 'YOUR_API_HASH'  # Replace with your API Hash
phone = 'YOUR_PHONE_NUMBER'  # Replace with your phone number

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

async def get_group_by_name(group_name):
    async with client:
        # Retrieve all dialogs
        dialogs = await client.get_dialogs()
        for dialog in dialogs:
            if dialog.name == group_name:  # Check if the dialog name matches the group name
                print(f'Found group "{dialog.name}" with ID: {dialog.id}')
                return dialog.id
        print(f'Group "{group_name}" not found.')

# Replace with the group name you want to search for
group_name = 'GROUP_NAME_TO_SEARCH'
client.loop.run_until_complete(get_group_by_name(group_name))
