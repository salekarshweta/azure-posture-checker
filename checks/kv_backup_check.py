def evaluate(keyvault_client):
    findings = []
    try:
        vaults = keyvault_client.vaults.list_by_subscription()
        for vault in vaults:
            # Resolving full vault metadata structures to trace underlying soft-delete states
            full_vault = keyvault_client.vaults.get(vault.id.split('/')[4], vault.name)
            enable_soft_delete = getattr(full_vault.properties, 'enable_soft_delete', False)
            if not enable_soft_delete:
                status = "FAIL"
                desc = "Key Vault missing soft-delete baseline configurations; vulnerable to ransomware erasure."
            else:
                status = "PASS"
                desc = "Vault soft-delete protection verified."
            findings.append({
                "check_id": "NO_BACKUP",
                "resource_type": "Microsoft.KeyVault/vaults",
                "resource_name": vault.name,
                "status": status,
                "description": desc
            })
    except Exception as e:
        print(f"[Rule Processing Warning] Failed pulling cryptographic vault descriptions: {e}")
    return findings