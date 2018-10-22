C:
cd "C:\my_folder"
get-childitem *.avi | foreach { rename-item $_ $_.Name.Replace(".tif", "") }