# INC-WSL2-0001 — WSL install returned HTTP 500

Date: 2026-09-21
Status: WORKAROUND_SUCCEEDED — reboot and post-reboot verification pending
Environment: Windows 11, WSL not previously installed

## Symptom

The operator ran:

```powershell
wsl --install -d Ubuntu-24.04
```

Observed output:

```text
Downloading: Windows Subsystem for Linux 2.7.14
Internal server error (500).
```

The command returned to the PowerShell prompt.

## Interpretation

The failure occurred while the WSL package was being downloaded. It did not indicate a GPU failure and did not prove that Windows virtualization was broken.

Microsoft documents `--web-download` as an alternative install source instead of the normal Microsoft Store-backed path.

## Visual decision flow

```mermaid
flowchart TD
    A[Run normal WSL install] --> B{Succeeds?}
    B -->|Yes| C[Restart if requested]
    B -->|No: HTTP 500| D[Run with --web-download]
    D --> E{Succeeds?}
    E -->|Yes| F[WSL installed + VirtualMachinePlatform enabled]
    F --> C
    E -->|No| G[Stop and collect exact error]
```

## Workaround used

The operator ran:

```powershell
wsl --install --web-download -d Ubuntu-24.04
```

Observed successful output included:

```text
Downloading: Windows Subsystem for Linux 2.7.14
Installing: Windows Subsystem for Linux 2.7.14
Windows Subsystem for Linux 2.7.14 has been installed.
Installing Windows optional component: VirtualMachinePlatform
[====================100.0%====================]
The operation completed successfully.
The requested operation is successful. Changes will not be effective until the system is rebooted.
```

Visual training asset:

`../installation/assets/wsl2-step-02-web-download-success.svg`

## Current next operator action

1. Save open Windows work.
2. Restart Windows normally.
3. Do not install Docker or any Growth OS service before post-reboot verification.
4. After reboot, launch Ubuntu 24.04 if it does not start automatically.
5. Then verify with:

```powershell
wsl --status
wsl --list --verbose
```

Expected final distribution state:

```text
Ubuntu-24.04    ...    VERSION 2
```

## Resolution criteria

This incident is not marked RESOLVED until all of these are verified:

- Windows has rebooted after enabling VirtualMachinePlatform.
- Ubuntu 24.04 initializes successfully.
- `wsl --status` succeeds.
- `wsl --list --verbose` shows Ubuntu 24.04 using WSL version 2.

## Safety

Do not run uninstall, unregister, DISM removal, Docker installation, or Ubuntu cleanup commands while the machine is waiting for this required reboot.

## Official references

- Microsoft Learn — Install WSL
- Microsoft Learn — Basic commands for WSL
- Microsoft Learn — Manual installation steps for problematic install paths
