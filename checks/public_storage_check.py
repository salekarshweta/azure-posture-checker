def evaluate(storage_client):
    findings = []
    try:
        # Pull all storage accounts in the subscription context
        storage_accounts = storage_client.storage_accounts.list()
        for account in storage_accounts:
            # Check if public access to blobs is enabled
            public_access_allowed = getattr(account, 'allow_blob_public_access', False)
            
            findings.append({
                "check_id": "PUBLIC_STORAGE",
                "resource_type": "Microsoft.Storage/storageAccounts",
                "resource_name": account.name,
                "status": "FAIL" if public_access_allowed else "PASS",
                "description": "Storage account permits anonymous public reading channels." if public_access_allowed else "Anonymous public access is strictly restricted."
            })
    except Exception as e:
        print(f"Warning: Couldn't scan storage metrics: {e}")
    return findings