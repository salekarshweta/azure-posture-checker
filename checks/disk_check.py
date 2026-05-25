def evaluate(compute_client):
    findings = []
    try:
        # Fetch all managed disks in the subscription
        disks = compute_client.disks.list()
        for disk in disks:
            # Check if Server-Side Encryption is set to PlatformManagedKey or CustomerManagedKey
            encryption_type = getattr(getattr(disk, 'encryption', None), 'type', None)
            is_secure = encryption_type is not None
            
            findings.append({
                "check_id": "UNENCRYPTED_DISKS",
                "resource_type": "Microsoft.Compute/disks",
                "resource_name": disk.name,
                "status": "PASS" if is_secure else "FAIL",
                "description": "Disk encryption is active." if is_secure else "Disk is not encrypted at rest."
            })
    except Exception as e:
        print(f"Warning: Couldn't scan disks: {e}")
    return findings