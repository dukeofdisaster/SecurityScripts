
# First we have to declare a variable that points to the actual file we wnat to edit
$LogFile = "C:\Users\user\Documents\captLog.txt"

#Then we need to define a function that caries out actions  on this file
# Our function has 1 string paramater logstring

Function log {

Param ([string]$logstring)

#We create a stamp variablee that uses the ps. command Get-Date and formats it
$Stamp = (Get-Date).toString("yyyy/MM/dd HH:mm:ss")

# We then create a variable called Line that consists of our Stamp and logstring variables 
$Line = "$Stamp $logstring"

# Finally, our function calls the ps Add-content function  on our $LogFile variable with the -Value flag and passes
# it the Line variable. 

Add-content $LogFile -Value $Line
}
