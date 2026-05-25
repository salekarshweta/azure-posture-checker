# Azure Posture Automation Engine (`azure-posture-checker`)

A modular Python Command Line Interface (CLI) security auditing tool engineered to evaluate live cloud posture states against infrastructure hardening baselines. This application automates Cloud Security Posture Management (CSPM) by querying live Azure resource APIs to intercept configuration drift and safety gaps.

---

## 📋 Project Prerequisites

Before running the application, ensure your local workstation has the following components configured:
1. **Python 3.10+**: Ensure Python 3 is installed and accessible via your system path.
2. **Azure Subscription**: A live active Azure account (Free Tier or Enterprise) containing resources to audit.
3. **Dependencies**: The required SDK libraries must be deployed in your workspace environment.

---

## 🔑 How to Authenticate

The application utilizes an advanced **Interactive Browser-Driven Authentication Callback Flow**. This approach eliminates the requirement of passing plaintext credentials or managing complex CLI configurations locally.

1. Locate and copy your target **Subscription ID** from your Azure Portal Dashboard.
2. Run the environment variable assignment command directly inside your active terminal window:
   ```powershell
   $env:AZURE_SUBSCRIPTION_ID="your-azure-subscription-id-here"
3. When the script executes, it initializes an isolated OAuth2 token request. A secure web browser window will automatically launch on your screen.
4. Log into your official Microsoft Azure account via the browser interface.
5. Once complete, the browser will safely hand the cryptographic access token back to your running Python process and close the session.

## 🏗️ Architectural Overview & Data Flow

The engine is built on the **Separation of Concerns** principle. Rather than operating as a monolithic script, the system is completely decoupled into modular, autonomous layers:

* **Authentication Token Layer (`auth.py`):** Instantiates an isolated OAuth2 token callback handshake with Microsoft's Identity provider utilizing browser redirection.
* **Core Conductor Orchestrator (`checker.py`):** Acts as the central system general manager. It safely binds the active subscription context and injects specialized SDK management clients down into the individual check processors.
* **Granular Policy Suite (`/checks`):** A plug-and-play directory containing independent inspection rules. Each module parses live resource metadata properties and appends standardized telemetry responses.
* **UI Presentation Layer (`output.py`):** Captures raw evaluation matrices and pipes them into a human-readable dashboard or structures raw machine-readable streams based on terminal parameters.

---
## 🏭 Production Deployment Note (Service Principals)
While interactive browser login is ideal for local engineering workflows, production architectures (such as unattended CI/CD automation pipelines) should utilize a Service Principal. To transition to a non-interactive flow, you would generate a secure identity profile in Entra ID and map the following credentials to your server environment:

AZURE_CLIENT_ID

AZURE_CLIENT_SECRET

AZURE_TENANT_ID


## 🚀 How to Run

1. Project Initialization

Clone your repository layout and configure an isolated virtual environment to prevent package collisions:

# Navigate to the workspace directory
cd d/azure-posture-checker

# Set up an isolated environment environment
python -m venv .venv

# Activate the workspace execution frame
.venv\Scripts\Activate.ps1

2. Dependency Resolution

Deploy the complete resource framework manifest into your active workspace environment:
pip install -r requirements.txt

3. Execution Commands

* Standard User Interface Run: Processes your subscription data points and prints a clear, color-coded interactive table grid layout:

python checker.py

* Stretch Goal — Automated CI JSON Pipeline Run: Suppresses formatting frames to deliver an unformatted machine-readable JSON array stream for external programmatic integrations:

python checker.py --json

## 🛡️ Explanation of Implemented Checks

The script contains independent scanning modules engineered to flag specific compliance failures:

# Check ID    --    Target Resource Component   --   Vulnerability Detection Logic &Impact

OPEN_PORTS    --   Microsoft.Network/networkSecurityGroups --  Scans inbound firewall rule architectures to intercept open management entry points (Ports 22 for SSH / 3389 for RDP) exposed to the public internet (0.0.0.0/0).

PUBLIC_STORAGE	-- Microsoft.Storage/storageAccounts --	Audits access tier properties to catch storage nodes explicitly allowing unauthenticated, anonymous blob data read traffic.

UNENCRYPTED_DISKS -- Microsoft.Compute/disks -- Evaluates block-level storage disks to confirm that native server-side encryption layers are actively configured.

NO_BACKUP -- Microsoft.KeyVault/vaults -- Assesses cryptographic secrets vaults to ensure data recovery protections—such as Soft-Delete safety nets—are operational.

## 📸 Sample Terminal Output Dashboard

(../output.png)

## 🛠️ How to Extend with New Checks

The system architecture is strictly decoupled based on the Separation of Concerns principle, allowing you to introduce a new policy rule in two quick steps without refactoring core code:

# Step 1: Create a Separate Check Module

Add a new .py script directly inside your /checks subfolder (e.g., checks/mfa_check.py) containing a standardized evaluate() function receiving its designated client:


def evaluate(graph_client):
    """Rule: Identify user identities operating without active multi-factor verification policy metrics."""
    findings = []
    # Query your resource models and populate the findings array...
    return findings

# Step 2: Register Module with Conductor Engine

Open the core orchestrator script (checker.py). Import your file, instantiate its matching SDK client framework dependency, and register it to the results list:


from checks import mfa_check
   ''Inside run_scanner()... ''
graph_client = get_azure_client(GraphRbacManagementClient)
all_findings.extend(mfa_check.evaluate(graph_client))
The central orchestrator engine will handle token deliveries, gather metrics, and dynamically print your findings to the main display table!