# Author: Adge Denkers (github.com/adgedenkers)
# Date: 2024-07-03
# Version: 1.0

import requests
from adal import AuthenticationContext
import os

TENANT = 'your-tenant-id'
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
RESOURCE = 'https://your-tenant-name.sharepoint.com'
AUTHORITY_URL = f'https://login.microsoftonline.com/{TENANT}'
SHAREPOINT_URL = 'https://your-tenant-name.sharepoint.com'
SITE_URL = f'{SHAREPOINT_URL}/sites/your-site'
DOCUMENT_LIBRARY = 'Shared Documents'
FILE_NAME = 'example.txt'
LOCAL_PATH = './downloads/'

def get_access_token():
    context = AuthenticationContext(AUTHORITY_URL)
    token = context.acquire_token_with_client_credentials(RESOURCE, CLIENT_ID, CLIENT_SECRET)
    return token['accessToken']

def download_file(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json;odata=verbose'
    }
    file_url = f'{SITE_URL}/_api/web/GetFileByServerRelativeUrl(\'/{DOCUMENT_LIBRARY}/{FILE_NAME}\')/$value'
    response = requests.get(file_url, headers=headers)
    if response.status_code == 200:
        if not os.path.exists(LOCAL_PATH):
            os.makedirs(LOCAL_PATH)
        with open(os.path.join(LOCAL_PATH, FILE_NAME), 'wb') as file:
            file.write(response.content)
        print(f'File {FILE_NAME} downloaded successfully.')
    else:
        print(f'Failed to download file. Status code: {response.status_code}')

if __name__ == '__main__':
    token = get_access_token()
    download_file(token)
