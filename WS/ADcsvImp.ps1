# Specify the path for the CSV file
$csvPath = "C:\Path\To\Import\Users.csv"

# Specify the path to the target Organizational Unit
$ouPath = "OU=Anvandare,OU=Enskede,DC=jultomten,DC=nu"

try {
    # Import user data from the CSV file
    $userData = Get-Content -Path $csvPath -Encoding UTF8 | Select-Object -Skip 1 | ConvertFrom-Csv -Header FirstName, Surname, City, Title

    # Create each user in Active Directory
    foreach ($user in $userData) {
        # Generate a SamAccountName and UserPrincipalName from the FirstName and Surname
        $firstNameForLogon = $user.FirstName.ToLowerInvariant() -replace 'å', 'a' -replace 'ä', 'a' -replace 'ö', 'o' -replace 'Å', 'A' -replace 'Ä', 'A' -replace 'Ö', 'O'
        $surnameForLogon = $user.Surname.ToLowerInvariant() -replace 'å', 'a' -replace 'ä', 'a' -replace 'ö', 'o' -replace 'Å', 'A' -replace 'Ä', 'A' -replace 'Ö', 'O'
        $samAccountName = $firstNameForLogon + "." + $surnameForLogon
        $userPrincipalName = $samAccountName + "@jultomten.nu"

        # Generate a password
        $securePassword = ConvertTo-SecureString -AsPlainText "Linux4Ever" -Force

        # Create the user
        New-ADUser -SamAccountName $samAccountName `
                   -UserPrincipalName $userPrincipalName `
                   -Name ($user.FirstName + " " + $user.Surname) `
                   -GivenName $user.FirstName `
                   -Surname $user.Surname `
                   -Enabled $true `
                   -DisplayName ($user.FirstName + " " + $user.Surname) `
                   -Path $ouPath `
                   -AccountPassword $securePassword `
                   -City $user.City `
                   -Title $user.Title

        Write-Host "User $samAccountName created"
    }
}
catch {
    Write-Host "An error occurred: $_"
}