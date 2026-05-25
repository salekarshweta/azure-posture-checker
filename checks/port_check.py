def evaluate(compute_client):
    findings = []
    try:
        nsgs = compute_client.network_security_groups.list_all()
        for nsg in nsgs:
            is_secure = True
            desc = "Management access points restricted safely."
            for rule in getattr(nsg, 'security_rules', []):
                if rule.access.lower() == 'allow' and rule.direction.lower() == 'inbound':
                    dest_port = str(rule.destination_port_range)
                    src_address = str(rule.source_address_prefix)
                    if dest_port in ['22', '3389', '*'] and src_address in ['*', '0.0.0.0/0', 'Internet']:
                        is_secure = False
                        desc = f"Insecure rule '{rule.name}' exposes port {dest_port} globally."
                        break
            findings.append({
                "check_id": "OPEN_PORTS",
                "resource_type": "Microsoft.Network/networkSecurityGroups",
                "resource_name": nsg.name,
                "status": "PASS" if is_secure else "FAIL",
                "description": desc
            })
    except Exception as e:
        print(f"[Rule Processing Warning] Failed scanning network security group components: {e}")
    return findings