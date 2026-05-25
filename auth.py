import os
import sys
from azure.identity import DefaultAzureCredential

def get_subscription_id():
    """Retrieves the active Azure Subscription ID from environment variables."""
    sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    if not sub_id:
        print("[Error] Missing AZURE_SUBSCRIPTION_ID environment variable.")
        sys.exit(1)
    return sub_id

def get_azure_client(client_class):
    """Instantiates an official Azure Management client using DefaultAzureCredential."""
    try:
        credential = DefaultAzureCredential()
        subscription_id = get_subscription_id()
        return client_class(credential, subscription_id)
    except Exception as e:
        print(f"[Auth Error] Failed to initialize Azure SDK client framework: {e}")
        sys.exit(1)