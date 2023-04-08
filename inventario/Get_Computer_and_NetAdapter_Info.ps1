$nomearquivocomp = $env:USERNAME + "_" + $env:COMPUTERNAME + "_ComputerInfo_"
$nomearquivoadapt = $env:USERNAME + "_" + $env:COMPUTERNAME + "_NetAdapter_"


Get-ComputerInfo | ConvertTo-Json | Out-File -FilePath $HOME\$nomearquivocomp.json
Get-NetAdapter | ConvertTo-Json | Out-File -FilePath $HOME\$nomearquivoadapt.json
wmic path win32_VideoController get name
wmic memorychip list full
get-physicaldisk | format-table -autosize