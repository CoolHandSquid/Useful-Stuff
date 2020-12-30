$myshell = New-Object -com "Wscript.Shell"
while ($true) {
  Start-Sleep -Seconds 10
  $myshell.sendkeys(".")
}
clear
