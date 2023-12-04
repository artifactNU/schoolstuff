# Import the GroupPolicy module
Import-Module GroupPolicy

# Specify the path for the GPO report
$gpoReportPath = "C:\Path\to\GPOAllReport.html"

# Generate the GPO report
Get-GPOReport -All -ReportType Html -Path $gpoReportPath

Write-Host "GPO report exported to $gpoReportPath"