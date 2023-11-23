# Specify the path to the target Organizational Unit
$ouPath = "OU=Users,DC=example,DC=com"

# Specify the path for the CSV file
$csvPath = "C:\Path\To\Export\Users.csv"

try {
    # Get user information in the specified OU
    $users = Get-ADUser -Filter * -SearchBase $ouPath -Properties SamAccountName, DisplayName, Email, Title, Department, Manager

    # Export user information to CSV
    $users | Select-Object SamAccountName, DisplayName, Email, Title, Department, Manager | Export-Csv -Path $csvPath -NoTypeInformation

    Write-Host "User information exported to $csvPath"

    # Check the CSV file to ensure the data was exported correctly
    $csvContent = Import-Csv -Path $csvPath
    $csvContent | Format-Table
}
catch {
    Write-Host "An error occurred: $_"
}