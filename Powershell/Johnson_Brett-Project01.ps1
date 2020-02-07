#Script to create a series of folders from a user defined path. The folders are numbered, appended to the end, and the proper number of zeros are added so that they sort correctly.

#Ask for inputs; path, new folder name, start, and end numbers.
$path = Read-Host "What is the path in which to create the folder(s)?"
$prefix = Read-Host "What is the first part of the new folder name? Include any characters you want appended before the number; spaces, dashes, etc."
$start = Read-Host "Beginning number?"
$end = Read-Host "End number?"


#Change inputs to integers where appropriate
$startInt = [int]$start
$endInt = [int]$end


#Loop to create multiple folders, incrementing by one each time
For ($i=$startInt; $i -le $endInt; $i++)
{
    #number of zeros to add; equal to difference of length of $i and $endInt
    $noOfZeros = ($endInt.tostring().length - $i.tostring().length)

    #add zeros to prefix
    $prefixWithZeros = $prefix.PadRight($prefix.length + $noOfZeros, '0')
    
    #append the integer to the string
    $folderName = $prefixWithZeros + $i

    #Make the directory path
    $newPath = Join-Path $path $folderName

    #Make the directory
    md -Path $newPath

}