# Import the GroupPolicy module
Import-Module GroupPolicy

# Specify the name of the GPO
$gpoName = "Your GPO Name"

# Specify the path for the GPO report
$gpoReportPath = "C:\Path\to\GPOSpecReport.html"

# Generate the GPO report
Get-GPOReport -Name $gpoName -ReportType Html -Path $gpoReportPath

Write-Host "GPO report for $gpoName exported to $gpoReportPath"