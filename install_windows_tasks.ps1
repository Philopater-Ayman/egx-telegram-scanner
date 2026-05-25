$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = "python"
$scanner = Join-Path $projectRoot "trading_bot_core.py"

$tasks = @(
    @{ Name = "EGX Scanner Open Prep"; Time = "09:15" },
    @{ Name = "EGX Scanner Midday"; Time = "12:00" },
    @{ Name = "EGX Scanner Post Close"; Time = "15:30" }
)

foreach ($task in $tasks) {
    $action = "cd /d `"$projectRoot`" && $python `"$scanner`""
    schtasks /Create /F /SC WEEKLY /D SUN,MON,TUE,WED,THU /TN $task.Name /TR "cmd /c $action" /ST $task.Time | Out-Host
}

Write-Host "Installed EGX scanner scheduled tasks for Sunday-Thursday."
Write-Host "Review Windows Task Scheduler if EGX changes hours, holidays, or Ramadan schedule."
