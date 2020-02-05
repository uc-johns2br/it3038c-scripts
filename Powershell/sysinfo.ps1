function getIP{
    (Get-NetIPAddress).IPAddress | Select-String "192"
}

function getDate{
    Get-Date -UFormat "%A, %B %d, %Y"  
}


$IP = getIP
$USER = $env:USERNAME
$HOSTNAME = $env:USERDOMAIN
$VERSION = $Host.Version.Major
$DATE = getDate


$BODY = "This machine's IP is $IP. User is $USER. Hostname is $HOSTNAME. PowerShell Version $VERSION. Today's Date is $DATE."

Send-MailMessage -To "brettjohnson791@gmail.com" -from "me@mail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -Port 587 -UseSsl -Credential (Get-Credential)

write-host("Email sent.")