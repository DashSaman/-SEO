$ErrorActionPreference = 'Stop'

# Keep the plugged-in pilot host awake.
powercfg /change standby-timeout-ac 0

# Start WSL at user logon without requiring an elevated Scheduled Task.
$StartupDir = [Environment]::GetFolderPath('Startup')
$Launcher = Join-Path $StartupDir 'GrowthOS-Start-WSL.cmd'
@"
@echo off
wsl.exe -d Ubuntu-24.04 --exec /bin/true
"@ | Set-Content -Path $Launcher -Encoding ASCII

$AcSleep = (powercfg /query SCHEME_CURRENT SUB_SLEEP STANDBYIDLE | Select-String 'Current AC Power Setting Index').Line
if ($AcSleep -notmatch '0x00000000') {
    throw 'AC sleep was not disabled.'
}
if (-not (Test-Path $Launcher)) {
    throw 'Startup launcher was not created.'
}

Get-Item $Launcher | Select-Object FullName,Length
Write-Output 'GROWTHOS_STARTUP_OK'
