
# Infrastructure Setup

This module covers the initial setup of the KnowledgeNet environment, integrating Obsidian, Google Colab, and GitHub.

## The KnowledgeNet Philosophy

This setup creates a **synergetic ecosystem** where three specialized tools interact to form a robust workflow for learning and documenting:

* **Obsidian (The Brain & Editor):** This is the heart of the system. It serves two vital purposes:
  1. **The Master Network:** A private, non-hierarchical space where all thoughts are linked bidirectionally.
  2. **Content Creation:** The primary environment for writing all documentation in Markdown format, turning isolated notes into a cohesive knowledge web.
* **Google Colab (The Code Laboratory):** A dedicated space for technical exploration. It is used exclusively for executing code, running simulations, or testing Python scripts, acting as an external "sandbox" for data-driven insights.
* **GitHub (The Archive & Showcase):** The layer for persistence and communication. It provides version control as a safety net and acts as a professional "shop window" to share curated expertise while maintaining full authority over the content.

## 1. Obsidian Installation & Setup (The Foundation)

> **Note:** On Ubuntu 22.04+, AppImages require the FUSE library to run.

**Action:** Install the necessary driver and prepare the application:

```bash
sudo apt update && sudo apt install libfuse2 -y
```

1. Download Obsidian (AppImage) from the official site.
2. Move it to your `~/Programs` folder.
3. Make it executable:

```bash
chmod +x ~/Programs/Obsidian-*.AppImage
```

> **Tip:** The `~` symbol is a shortcut for your home directory (e.g., `/home/USER/`). You can type it directly into the terminal.

### Directory Structure & Privacy
To separate private thoughts (Master Network) from public documentation (Content), we use a nested vault strategy.

* **Master Vault (Private):** `~/AppData/ObsidianVaults/KnowledgeNet`
* **Public Vault (GitHub):** `~/AppData/ObsidianVaults/KnowledgeNet/KnowledgeNetPublic`

**Action:** Prevent Git from tracking private data by creating a `.gitignore` in the Master Vault. This ensures the public repository stays separate:

```bash
cd ~/AppData/ObsidianVaults/KnowledgeNet
echo "KnowledgeNetPublic/" > .gitignore
```

## 2. Google Colab Setup (The Laboratory)

> **Concept:** Colab is used specifically for code execution and interactive experiments.

1. Open [Google Colab](https://colab.research.google.com).
2. Create a new notebook.
3. Rename it to `Infrastructure.ipynb`.
4. Use this space for any code-heavy modules that require a cloud-based Python environment.

## 3. GitHub Synchronization (The Archive)

### Step 1: Account & Repository Creation
1. **Create Account:** If you don't have one, sign up at [github.com](https://github.com/).
   * **Note:** Remember the **email address** and **username** you use here; they are required for setting up the automated identification of your data backups in Step 3.
1. **Create Repository for Public Vault:** - Click the **"+"** icon (top right) -> **New repository**.
   - Name it `KnowledgeNetPublic`.
   - Set visibility to **Public**.
   - **Important:** Do NOT initialize with a README, license, or .gitignore (we will do this via terminal).
   - Click **Create repository.**
   - for Private Vault:**.
   - **Create Repository for Private Vault** as described above, with the following changes:
	   - name it `KnowledgeNet`.
	   - Set visibility to **Private**

### Step 2: Generating a Personal Access Token (PAT)
Since GitHub deprecated password authentication for terminal operations, you must use a PAT.

1. Go to **Settings** on GitHub (top right profile icon).
2. Scroll down to **Developer settings** (left sidebar).
3. Select **Personal access tokens** -> **Tokens (classic)**.
4. Click **Generate new token (classic)**.
5. **Setup:** Give it a name (e.g., "Obsidian Sync"), set an expiration, and select the **'repo'** scope.
6. **Important:** Copy the token immediately! You won't see it again. (It usually starts with `ghp_` followed by many characters).

> **Tip (Credential Helper):** To avoid pasting your token for every single push, run this command in your Ubuntu terminal:

```bash
git config --global credential.helper store
```

### Step 3: Global Git Configuration
To enable automated synchronization and identify your backups, Git needs to know your identity. Run these commands once in your terminal using the credentials from Step 1:

```bash
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"
```

### Step 4: Final Action (Initialize & Push)
Now, connect your local folder to the cloud repository:

```bash
cd ~/AppData/ObsidianVaults/KnowledgeNet/KnowledgeNetPublic
git init
git branch -M main
git add .
git commit -m "Initial infrastructure documentation"
git remote add origin https://github.com/YOUR_USERNAME/KnowledgeNetPublic.git
git push -u origin main
```

*Note: When prompted for a password, paste your **PAT**, not your GitHub password.*

### Step 5: Initializing the Private Backup
The Master Vault was initialized as a separate Git repository to secure all private notes:

cd ~/AppData/ObsidianVaults/KnowledgeNet
git init
git add .
git commit -m "Initial private setup"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/KnowledgeNet.git
git push -u origin main

## 5. Automation with Obsidian Git (Optional)

To avoid manual terminal commands for every update, the **Obsidian Git** community plugin is used.

1. **Install:** Settings -> Community Plugins -> Browse -> "Obsidian Git".
2. **Setup:** - **Vault backup interval:** Set to 10-30 minutes for auto-sync.
   - **Commit message:** Default to {{date}}.
1. **Usage:** Look for the Git icon in the left sidebar to see pending changes or click to push manually.