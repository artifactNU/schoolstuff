<#
.SYNOPSIS
    This script reads a file and returns
    all lines that do not start with a comment.
.DESCRIPTION
    This script reads a file and returns
    all lines that do not start with a hash
    character (#). If a search word is provided,
    only lines containing the search word are
    returned.
.PARAMETER InputString
    The string to be processed.
.EXAMPLE
    PS> .\effective.ps1 -File .\example.txt
    This will return all lines in example.txt that do not start with a hash character.
.EXAMPLE
    PS> .\effective.ps1 -SearchWord "foo" -File .\example.txt
    This will return all lines in example.txt that do not start with a hash character and contain the word "foo".
#>


param(
    [Parameter(Mandatory)]
    [ValidateScript({ Test-Path -PathType Leaf $_  }, ErrorMessage = "File not found or not a regular file")]
    [string]$File,
    [string]$SearchWord
)

$Path = Resolve-Path $File

if ($SearchWord) {
    Get-Content $Path | Where-Object { $_ -notmatch '^\s*#' -and $_ -match $SearchWord }
} else {
    Get-Content $Path | Where-Object { $_ -notmatch '^\s*#' }
}

