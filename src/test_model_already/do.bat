echo Run Tesseract for Training.. 
tesseract.exe model0.tif model0 nobatch box.train 

echo Compute the Character Set.. 
unicharset_extractor.exe model0.box 
mftraining -F font_properties -U unicharset -O num.unicharset model0.tr 


echo Clustering.. 
cntraining.exe model0.tr 

echo Rename Files.. 
rename normproto num.normproto 
rename inttemp num.inttemp 
rename pffmtable num.pffmtable 
rename shapetable num.shapetable  

echo Create Tessdata.. 
combine_tessdata.exe num. 

echo. & pause
