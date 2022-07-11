from storages.backends.azure_storage import AzureStorage
import os;

class AzureMediaStorage(AzureStorage):
    account_name = os.environ.get('AZURE_ACCOUT_NAME',)  # Must be replaced by your <storage_account_name>
    account_key = os.environ.get('AZURE_ACCOUNT_PASS') # Must be replaced by your <storage_account_key>
    azure_container = 'django-blog-files'
    expiration_secs = None