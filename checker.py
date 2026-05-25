import argparse
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.network import NetworkManagementClient

from auth import get_azure_client
from output import render_screen_results
from checks import port_check, disk_check, public_storage_check, kv_backup_check

def run_scanner(json_output=False):
    all_findings = []

    # 2. INITIALIZE THE NETWORK CLIENT HERE
    network_client = get_azure_client(NetworkManagementClient)
    compute_client = get_azure_client(ComputeManagementClient)
    storage_client = get_azure_client(StorageManagementClient)
    keyvault_client = get_azure_client(KeyVaultManagementClient)

    # 3. PASS THE network_client TO port_check
    all_findings.extend(port_check.evaluate(network_client))
    all_findings.extend(disk_check.evaluate(compute_client))
    all_findings.extend(public_storage_check.evaluate(storage_client))
    all_findings.extend(kv_backup_check.evaluate(keyvault_client))

    render_screen_results(all_findings, export_json=json_output)

def main():
    parser = argparse.ArgumentParser(description="Live Azure CSPM Auditing CLI Engine.")
    parser.add_argument("--json", action="store_true", help="Format findings into JSON.")
    args = parser.parse_args()
    run_scanner(json_output=args.json)

if __name__ == "__main__":
    main()