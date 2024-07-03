
## How to Download a file from SharePoint using Python


In this tutorial, we'll guide you through the process of creating an application in SharePoint using the SharePoint UI, registering it, and then using the application credentials to connect to a SharePoint site's document library. Finally, we'll copy a file from the document library to your local machine using Python.

### Prerequisites

1. A SharePoint Online site.
2. Site Collection Administrator access to the SharePoint site.
3. Python installed on your local machine.
4. `Office365-REST-Python-Client` library installed. You can install it using pip:
   ```sh
   pip install Office365-REST-Python-Client
   ```

### Step 1: Create a SharePoint Application

1. **Navigate to App Registration Page:**
   Open your browser and go to the following URL:
   ```
   https://[your-tenant].sharepoint.com/sites/[your-site]/_layouts/15/AppRegNew.aspx
   ```
   Replace `[your-tenant]` and `[your-site]` with your actual SharePoint tenant and site name.

2. **Register a New App:**
   Fill in the following details:
   - **Client Id:** Click "Generate" to create a new client ID.
   - **Client Secret:** Click "Generate" to create a new client secret. Save this secret securely as it will not be shown again.
   - **Title:** Enter a name for your application.
   - **App Domain:** You can use "localhost" for testing purposes.
   - **Redirect URI:** Enter `https://localhost`.

3. **Save the App Information:**
   Click "Create" and note down the **Client Id** and **Client Secret**. You’ll need these for authentication.

### Step 2: Grant Permissions to the App

1. **Navigate to App Permissions Page:**
   Open your browser and go to:
   ```
   https://[your-tenant].sharepoint.com/sites/[your-site]/_layouts/15/appinv.aspx
   ```
   Replace `[your-tenant]` and `[your-site]` with your actual SharePoint tenant and site name.

2. **Enter App Information:**
   - **App Id:** Enter the Client Id you generated in Step 1 and click "Lookup". The app’s details should appear below.

3. **Define App Permissions:**
   In the **Permission Request XML** box, enter the following XML to request the necessary permissions:
   ```xml
   <AppPermissionRequests>
     <AppPermissionRequest Scope="http://sharepoint/content/sitecollection" Right="Read" />
     <AppPermissionRequest Scope="http://sharepoint/content/sitecollection/web" Right="Read" />
   </AppPermissionRequests>
   ```

4. **Grant Permissions:**
   Click "Create". You will be prompted to trust the app. Click "Trust It".

### Step 3: Access SharePoint Document Library Using Python

Now that we have our application set up and registered, we can use its credentials to connect to the SharePoint site and interact with the document library.

#### Python Script to Copy a File from SharePoint to Local Machine

Create a Python script named `copy_sharepoint_file.py` and add the following code:

```python
# Author: Adge Denkers (github.com/adgedenkers)
# Date: 2024-07-03
# Version: 1.0

from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
import os

# SharePoint site and document library details
site_url = "https://[your-tenant].sharepoint.com/sites/[your-site]"
document_library = "Shared Documents"
file_name = "example.docx"  # The file you want to copy
local_path = os.path.join(os.getcwd(), file_name)

# Application credentials
client_id = "[your-client-id]"
client_secret = "[your-client-secret]"

# Authenticate and connect to SharePoint
ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))

# Get the file from the document library
file_url = f"/sites/[your-site]/{document_library}/{file_name}"
response = ctx.web.get_file_by_server_relative_url(file_url).download(local_path).execute_query()

print(f"File '{file_name}' has been downloaded to '{local_path}'")
```

Replace the placeholders (`[your-client-id]`, `[your-client-secret]`, `[your-tenant]`, `[your-site]`, and `example.docx`) with your actual SharePoint details and credentials.

### Step 4: Run the Python Script

Open a terminal or command prompt, navigate to the directory containing `copy_sharepoint_file.py`, and run the script:

```sh
python copy_sharepoint_file.py
```

If everything is set up correctly, the script will download the specified file from your SharePoint document library to your local machine.

### Conclusion

In this tutorial, you learned how to create and register a SharePoint application using the SharePoint UI, configure its permissions, generate a client secret, and use the credentials to connect to a SharePoint site's document library using Python. This process can be a foundation for more complex SharePoint interactions in your applications.

For more detailed information on the SharePoint API, refer to the [Microsoft Graph API documentation](https://docs.microsoft.com/en-us/graph/overview).

If you have any questions or need further assistance, feel free to reach out in the comments or refer to the additional resources linked below.

#### Additional Resources:
- [Office365-REST-Python-Client GitHub Repository](https://github.com/vgrem/Office365-REST-Python-Client)
- [SharePoint API Documentation](https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/working-with-folders-and-files-with-rest)
