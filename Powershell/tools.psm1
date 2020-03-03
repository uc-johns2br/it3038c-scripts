function getIP{
    $IP = Get-NetIPAddress | Where-Object {$_.IPv4Address -like '192*'}
}