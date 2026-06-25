<#
.SYNOPSIS
  安装知识库每日自动抓取计划任务
.DESCRIPTION
  创建 Windows 计划任务，每天 9:00 和 14:00 自动运行抓取脚本。
  可通过 -Time 参数自定义运行时间。
#>

param(
    [string[]]$Times = @("09:00", "14:00"),
    [string]$TaskName = "KnowledgeBaseDailyHarvester"
)

$ScriptPath = Join-Path $PSScriptRoot "daily_harvester.py"
$PythonPath = (Get-Command python).Source

# 检查脚本是否存在
if (-not (Test-Path $ScriptPath)) {
    Write-Error "脚本不存在: $ScriptPath"
    exit 1
}

# 删除已有任务（如果存在）
$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "⏹ 删除已有计划任务: $TaskName"
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

# 创建计划任务
$Action = New-ScheduledTaskAction -Execute $PythonPath -Argument "`"$ScriptPath`""
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

$Triggers = @()
foreach ($Time in $Times) {
    $Triggers += New-ScheduledTaskTrigger -Daily -At $Time
}

$Principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest

Register-ScheduledTask -TaskName $TaskName `
    -Action $Action `
    -Trigger $Triggers `
    -Settings $Settings `
    -Principal $Principal `
    -Description "知识库自动抓取 - 每天 $($Times -join ', ') 运行"

Write-Host ""
Write-Host "✅ 计划任务已创建: $TaskName"
Write-Host "   运行时间: 每天 $($Times -join ', ')"
Write-Host "   脚本路径: $ScriptPath"
Write-Host ""
Write-Host "手动运行测试: python `"$ScriptPath`""
Write-Host "立即触发任务: Start-ScheduledTask -TaskName `"$TaskName`""
