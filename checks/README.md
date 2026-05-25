# Azure Posture Automation Engine (`azure-posture-checker`)

A modular, enterprise-ready Python Command Line Interface (CLI) security auditing tool engineered to evaluate live cloud posture states against strict infrastructure hardening baselines. This application automates Cloud Security Posture Management (CSPM) by systematically querying Azure resource APIs to intercept configuration drift and severe security vulnerabilities before exploit vectors can be weaponized.

---

## 🔒 Implemented Security & Compliance Policies

The auditing engine evaluates target Azure subscriptions against a core multi-layer infrastructure baseline check suite:

| Check ID | Severity | Target Cloud Resource | Policy Verification Description & Business Impact |
| :--- | :--- | :--- | :--- |
| **`OPEN_PORTS`** | CRITICAL | `Microsoft.Network/networkSecurityGroups` | Intercepts inbound firewall rules exposing structural management entryways (Ports `22` for SSH / `3389` for RDP) to the wide-open public internet (`0.0.0.0/0`), preventing global brute-force access channels. |
| **`PUBLIC_STORAGE`** | HIGH | `Microsoft.Storage/storageAccounts` | Audits access tier configurations to identify active object storage instances permitting unauthenticated anonymous blob traffic, mitigating data exfiltration risks. |
| **`UNENCRYPTED_DISKS`** | HIGH | `Microsoft.Compute/disks` | Evaluates block-level virtual machine storage volumes to verify that active server-side envelope storage encryption metrics are operating at compliance baselines. |
| **`NO_BACKUP`** | MEDIUM | `Microsoft.KeyVault/vaults` | Assesses cryptographic secret and key store configurations to guarantee business continuity metrics—such as soft-delete and purge protection safety nets—are enabled. |

---

## 🏗️ Architectural Overview & Data Flow

The engine is built on the **Separation of Concerns** principle. Rather than operating as a monolithic script, the system is completely decoupled into modular, autonomous layers:

* **Authentication Token Layer (`auth.py`):** Instantiates an isolated OAuth2 token callback handshake with Microsoft's Identity provider utilizing browser redirection.
* **Core Conductor Orchestrator (`checker.py`):** Acts as the central system general manager. It safely binds the active subscription context and injects specialized SDK management clients down into the individual check processors.
* **Granular Policy Suite (`/checks`):** A plug-and-play directory containing independent inspection rules. Each module parses live resource metadata properties and appends standardized telemetry responses.
* **UI Presentation Layer (`output.py`):** Captures raw evaluation matrices and pipes them into a human-readable dashboard or structures raw machine-readable streams based on terminal parameters.

---

## 💻 Local Installation & Workspace Preparation

### Prerequisites
* Python 3.10 or higher installed locally.
* An active Azure Subscription context.

### 1. Workspace Configuration
Clone the repository and initialize a clean virtual environment wrapper to isolate third-party library dependencies:

```bash
# Clone the repository
git clone [https://github.com/salekarshweta/azure-posture-checker.git](https://github.com/salekarshweta/azure-posture-checker.git)
cd azure-posture-checker

# Initialize the virtual environment wrapper
python -m venv .venv

# Activate the isolated execution workspace
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux / macOS Terminal:
source .venv/bin/activate