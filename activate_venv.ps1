# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# .\activate_venv.ps1


$venvPath = ".\venv\Scripts\Activate.ps1"

if (Test-Path $venvPath) {
    & $venvPath
} else {
    Write-Host "Virtual environment not found at $venvPath"
}
