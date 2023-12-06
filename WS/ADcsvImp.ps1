# Specify the path for the CSV file
$csvPath = "C:\Path\To\Import\Users.csv"

try {
    # Import user data from the CSV file
    $userData = Get-Content -Path $csvPath -Encoding UTF8 | Select-Object -Skip 1 | ConvertFrom-Csv -Header FirstName, Surname, PhoneNumber, Address, Postcode, City, Title

    # Create each user in Active Directory
    foreach ($user in $userData) {
        # Generate a SamAccountName and UserPrincipalName from the FirstName and Surname
        $firstNameForLogon = $user.FirstName.ToLowerInvariant() -replace 'å', 'a' -replace 'ä', 'a' -replace 'ö', 'o' -replace 'Å', 'A' -replace 'Ä', 'A' -replace 'Ö', 'O' -replace 'é', 'e' -replace 'É', 'E' -replace 'Ü', 'u'  -replace ' ', '.'
        $surnameForLogon = $user.Surname.ToLowerInvariant() -replace 'å', 'a' -replace 'ä', 'a' -replace 'ö', 'o' -replace 'Å', 'A' -replace 'Ä', 'A' -replace 'Ö', 'O' -replace 'é', 'e' -replace 'É', 'E' -replace 'Ü', 'u'  -replace ' ', '.'
        $samAccountName = ($firstNameForLogon + "." + ($surnameForLogon.Split(' ')[0])).Substring(0, [Math]::Min(20, ($firstNameForLogon + "." + ($surnameForLogon.Split(' ')[0])).Length))
        $samAccountName = $samAccountName.TrimEnd('.') # Remove trailing dot
        $userPrincipalName = $samAccountName + "@jultomten.nu"

            # Determine the OU based on the city
    switch ($user.City) {
        "Stockholm" { $ouPath = "OU=Anvandare,OU=Stockholm,DC=jultomten,DC=nu" }
        "Sundsvall" { $ouPath = "OU=Anvandare,OU=Sundsvall,DC=jultomten,DC=nu" }
    }

        # Print the SamAccountName and UserPrincipalName to the console
        Write-Host "SamAccountName: $samAccountName"
        Write-Host "UserPrincipalName: $userPrincipalName"

        # Generate a password
        $securePassword = ConvertTo-SecureString -AsPlainText "Linux4Ever" -Force

# Create the user
New-ADUser -SamAccountName $samAccountName `
           -UserPrincipalName $userPrincipalName `
           -Name ($user.FirstName + " " + $user.Surname) `
           -GivenName $user.FirstName `
           -Surname $user.Surname `
           -Enabled $true `
           -Title $user.Title `
           -Description $user.Title `
           -StreetAddress $user.Address `
           -City $user.City `
           -PostalCode $user.Postcode `
           -OfficePhone $user.PhoneNumber `
           -AccountPassword $securePassword `
           -Path $ouPath
    }
}
catch {
    Write-Error "An error occurred: $_"
}