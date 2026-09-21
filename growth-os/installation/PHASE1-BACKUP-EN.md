# Phase 1 Baseline Backup — WSL2 / Ubuntu / Docker

This step is performed immediately before Phase 2 so the project has a known-good restore point containing Ubuntu 24.04, WSL2 configuration and the verified Docker runtime.

## Why take this backup?

Ubuntu, GPU visibility, WSL resource limits, systemd and Docker have now been verified. Phase 2 will add persistent services, databases and automation. This export provides a clean rollback point if a later deployment goes wrong.

## Step 1 — Exit Ubuntu

Inside Ubuntu:

```bash
exit
```

## Step 2 — Create a Windows backup directory

In PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path C:\GrowthOS-Backups
```

## Step 3 — Fully stop WSL

```powershell
wsl --shutdown
```

## Step 4 — Export the Ubuntu distribution

```powershell
wsl --export Ubuntu-24.04 C:\GrowthOS-Backups\Ubuntu-24.04-phase1-2026-09-21.tar
```

The export can take several minutes. Keep the terminal open until the prompt returns.

## Step 5 — Verify the file

```powershell
Get-Item C:\GrowthOS-Backups\Ubuntu-24.04-phase1-2026-09-21.tar | Format-List FullName,Length,LastWriteTime
```

## Step 6 — Record SHA256

```powershell
Get-FileHash C:\GrowthOS-Backups\Ubuntu-24.04-phase1-2026-09-21.tar -Algorithm SHA256
```

Record the size and hash in the execution ledger. Do not commit the backup archive itself to GitHub.

## Security note

The export may contain configuration and future secrets stored inside Ubuntu. Keep it private and out of the repository.

## Recovery principle

Recovery should be deliberate. Avoid destructive `wsl --unregister` actions during troubleshooting. Prefer importing a backup under a separate distribution name first, verify it, and only then decide whether to replace the active instance.
