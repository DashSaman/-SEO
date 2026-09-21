$ErrorActionPreference = 'Stop'

$raw = (wsl -d Ubuntu-24.04 -- hostname -I).Trim()
if (-not $raw) {
    throw 'Could not resolve the Ubuntu WSL address.'
}
$WslIp = $raw.Split(' ', [System.StringSplitOptions]::RemoveEmptyEntries)[0]

$Urls = @(
    "http://${WslIp}:8080",
    "http://${WslIp}:3001",
    "http://${WslIp}:5001"
)

foreach ($Url in $Urls) {
    $response = Invoke-WebRequest -UseBasicParsing -Uri $Url -TimeoutSec 10 -ErrorAction Stop
    if ($response.StatusCode -ne 200) {
        throw "Unexpected HTTP status for ${Url}: $($response.StatusCode)"
    }
}

Write-Output "Growth OS UIs verified on WSL address: $WslIp"
Write-Output "Activepieces: $($Urls[0])"
Write-Output "Uptime Kuma: $($Urls[1])"
Write-Output "Dockge: $($Urls[2])"

foreach ($Url in $Urls) {
    Start-Process $Url
}
