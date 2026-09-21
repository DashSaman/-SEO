$ErrorActionPreference = 'Stop'

powercfg /change standby-timeout-ac 0

$Action = New-ScheduledTaskAction -Execute 'wsl.exe' -Argument '-d Ubuntu-24.04 --exec /bin/true'
$Trigger = New-ScheduledTaskTrigger -AtLogOn
$Settings = New-ScheduledTaskSettingsSet -StartWhenAvailable
$Principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Highest

Register-ScheduledTask `
  -TaskName 'GrowthOS-Start-WSL' `
  -Action $Action `
  -Trigger $Trigger `
  -Settings $Settings `
  -Principal $Principal `
  -Description 'Start Ubuntu WSL for Growth OS services at user logon' `
  -Force

Get-ScheduledTask -TaskName 'GrowthOS-Start-WSL' | Select-Object TaskName, State
