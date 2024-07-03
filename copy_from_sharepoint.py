# Author: Adge Denkers (github.com/adgedenkers)
# Date: 2024-07-03
# Version: 1.0

from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
import os

# SharePoint Information
tenant_name = "example"
site_path = "mysite/subsite"
document_library = "received"

site_url = f"https://{tenant_name}.sharepoint.com/sites/{site_path}"

# The File you want to copy
file_name = "example.docx" 

# Application credentials
client_id = "[your-client-id]"
client_secret = "[your-client-secret]"

# Local Server Information
local_folder_path = "c:\\files"

# Save the file in the same directory as the script
# local_path = os.path.join(os.getcwd(), file_name)

# Save the file in a specific directory (set `local_folder_path` above)
local_path = os.path.join(local_folder_path, file_name)

# --- No Need to Edit Below Here ---

# Authenticate and connect to SharePoint
ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))

# Get the file from the document library
file_url = f"/sites/{site_path}/{document_library}/{file_name}"
response = ctx.web.get_file_by_server_relative_url(file_url).download(local_path).execute_query()

print(f"File '{file_name}' has been downloaded to '{local_path}'")
