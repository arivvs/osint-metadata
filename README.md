# Osint-metadata
Finds image metadata, then outputs it to the console and leaves a "Report" in the root folder where the script is installed

### !!! ATTENTION !!!
WHEN DOWNLOADING FILES FROM TG, INSTAGRAM, FACEBOOK, ETC., BE CAREFUL, AS METADATA IS OFTEN REMOVED AND CANNOT BE READ

Also, for the location function to work, it must be enabled by the person who took the photo; otherwise, the location will not be displayed

## Installation and Launch

### 1 Install dependencies using the command
```bash
pip install -r requirements.txt
```

### 2 Start script
```bash
python meta.py
```
## Script Operation
The console displays the message: "Enter the full path to the photo: ", where you need to specify the full path to the file, for example: "C:\Users\hqays\Desktop\test.jpg" (Enter the path without quotes). To make finding the path easier, you can press ctrl + shift + c to copy the path

After you press enter, the metadata is output to the console, along with the "Most Important" section, which specifies: ![Following information](https://i.imgur.com/x9IU4YL.png)

P.s. if the location tracking function is enabled, a link to the location on Google Maps is provided

All of this is also saved to the "osint-report.txt" file

## Disclaimer

This tool is developed solely for educational purposes and for conducting legal OSINT research. The author is not responsible for any illegal use of this software. Always comply with data protection laws (GDPR).
