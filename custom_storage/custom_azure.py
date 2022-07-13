from storages.backends.azure_storage import AzureStorage
import os;

class AzureMediaStorage(AzureStorage):
    account_name = os.environ.get('AZ_STORAGE_ACCOUNT_NAME')  # Must be replaced by your <storage_account_name>
    account_key = os.environ.get('AZ_STORAGE_ACCOUNT_KEY') # Must be replaced by your <storage_account_key>
    azure_container = 'django-blog-files'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = os.environ.get('AZ_STORAGE_ACCOUNT_NAME') # Must be replaced by your storage_account_name
    account_key = os.environ.get('AZ_STORAGE_ACCOUNT_KEY') # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None