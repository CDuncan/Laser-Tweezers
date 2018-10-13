E:
cd "Tracking\Day 5"
get-childitem *.csv | foreach { rename-item $_ $_.Name.Replace("_Camera_tr_Track", "") }