Library Sign-In Scanner Instructions

How to open and run the program
1. Open the file named "BarcodeScanner.cpython-310"
2. Use scanner to scan students ID's
3. After use, open the "List.txt" document and make sure to save it

How to exit program
1. Either click the red button or enter "exit" into the program

How to add a student manually
1. Enter the students LastName, FistName
-i.e. Domingo, Dylan
If student is new and their information is not in the system you may manualy
enter their information in the "List.txt" document.

OR

2. Have them manually write things down

How to convert Text Document to Google Sheet
1. Open an existing sheet in Google sheets
2. Go through File > Import > Upload > Browse
3. From here, find and upload the "List.txt" document into the sheet
4. Change the Import Location to "Append to current sheet"
5. Import data

How to update list of student barcodes
1. Retrieve file of new Student Barcodes as a .XLS file
2. Open the Student Barcodes file in Google Sheets
3. In the menu, hit File>Download>Comma Seperated Values (.csv)
4. Once the file is downloaded, rename the file to "Student Barcodes.csv"
5. Go to the "__pycache__" folder and replace the previous "Student Barcodes" file with the new one