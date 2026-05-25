import argparse
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.keyvault import KeyVaultManagementClient

from auth import get_azure_client
from output import render_screen_results

# Explicit relative imports of the check modules
from checks import port_check, disk_check, public_storage_check, kv_backup_check

def run_scanner(json_output=False):
    """Orchestrates live cloud queries across active resource groupings."""
    all_findings = []

    # Initialize live client bindings
    compute_client = get_azure_client(ComputeManagementClient)
    storage_client = get_azure_client(StorageManagementClient)
    keyvault_client = get_azure_client(KeyVaultManagementClient)

    # Invoke targeted resource scanning suites
    all_findings.extend(port_check.evaluate(compute_client))
    all_findings.extend(disk_check.evaluate(compute_client))
    all_findings.extend(public_storage_check.evaluate(storage_client))
    all_findings.extend(kv_backup_check.evaluate(keyvault_client))

    render_screen_results(all_findings, export_json=json_output)

def main():
    parser = argparse.ArgumentParser(description="Live Azure CSPM Auditing CLI Engine.")
    parser.add_argument("--json", action="store_true", help="Format findings into a machine-readable JSON object.")
    args = parser.parse_args()
    run_scanner(json_output=args.json)

if __name__ == "__main__":
    main()