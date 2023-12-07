# Import the Active Directory module
Import-Module ActiveDirectory

# Create the main OUs
$mainOUs = "Stockholm", "Sundsvall", "Resursgrupper", "Servrar"
foreach ($ou in $mainOUs) {
    New-ADOrganizationalUnit -Name $ou -Path "DC=fantasi,DC=nu"

    # Create the sub-OUs
    $subOUs = "Anvandare", "Datorer", "Grupper"
    foreach ($subOU in $subOUs) {
        New-ADOrganizationalUnit -Name $subOU -Path "OU=$ou,DC=fantasi,DC=nu"

        # Create additional sub-OUs under "Grupper"
        if ($subOU -eq "Grupper") {
            $grupperSubOUs = "Ledning", "Konsulter", "Saljare", "IT", "Ekonomi"
            foreach ($grupperSubOU in $grupperSubOUs) {
                New-ADOrganizationalUnit -Name $grupperSubOU -Path "OU=$subOU,OU=$ou,DC=fantasi,DC=nu"
            }
        }
    }
}