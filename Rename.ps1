C:
cd "C:\my_folder\Out"
get-childitem *.csv | foreach { rename-item $_ $_.Name.Replace("_Camera_tr_Track", "") }