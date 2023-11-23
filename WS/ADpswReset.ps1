# Specify the path to the target Organizational Unit
$ouPath = "OU=Users,DC=example,DC=com"

try {
    # Get all users in the specified OU
    $users = Get-ADUser -Filter * -SearchBase $ouPath

    # Reset the password for each user
    foreach ($user in $users) {
        # Generate a random password (customize this logic)
        $newPassword = ConvertTo-SecureString -AsPlainText "NewPassword123!" -Force

        # Set the new password for the user
        Set-ADAccountPassword -Identity $user -NewPassword $newPassword -Reset

        # Enable the user account (if it's disabled)
        if (!$user.Enabled) {
            Enable-ADAccount -Identity $user
        }

        Write-Host "Password reset for $($user.SamAccountName)"
    }
}
catch {
    Write-Host "An error occurred: $_"
}