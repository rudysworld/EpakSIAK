# EpakSIAK

**WELCOME** 

You might be wonderin what is "EpakSIAK" and how you can use it to hopefully win the SIAK war. Essentially "EpakSIAK" can help you constantly refresh and choose your classes for you increasing your chance of winning. Do remember you still have to manually submit the IRS, the reason for this is to minimize the risk of prematurely submitting it and instead having to do it all over again.


## Setup Instructions

### 1. Prerequisites

   - **Get Homebrew**: 

   - **Open Terminal**: Open command prompt or terminal depending on your operating system

   - **Get Python**: Obviously since EpakSIAK runs on Python, you need to have that installed on your device. Open cmd (Windows) or terminal and install python using:
```
brew install python
```

   - **Install TKinter**: If you're not using MacOS, don't worry about this since it's generally already installed on the windows/linux version of Python (although doing this step just to make sure it is up-to-date is still a good idea). For all you mac users however, use:
```
brew install python-tk
```

   - **Install chromedriver**: If you're on MacOS and If you're using this near the time as of me writing this (3 August 2024) don't worry about this since i have already installed it for you in this folder and it is still up to date. However, if not using MacOS or if you're using this after the 2024 2nd semester term, download it for the corrct corresponding device and chrome version then replace the driver in this folder with the new one.

   - **Navigate to the Folder**: In your cmd or terminal and change the directory to your EpakSIAK folder using:
```
cd epaksiak/siakwar
```

### 2. Libraries

   You’ll need a couple of Python libraries. Run the following commands in your terminal:
```
python3 -m pip install selenium
```
   Use venv if this doesnt work and/or if a error shows up. Do so by typing in:
```
python3 -m venv path/to/venv
source path/to/venv/bin/activate
python3 -m pip install selenium
```

### 3. Configure the `config.txt` File

   Open the `config.txt` file and update it with your SIAK username, password, and subject codes. You can find it by going to this folder. The subject codes can be find by hovering your cursor at your preferred class link. Also, don't forget to type in the number of SKS the specific class has or else this bot will not work.

### 4. Run the Program

   - Execute the program using the command:
```
     python EpakSIAK.py
```
   - The program will automatically open a browser window and try to log in using the credentials from `config.txt`.
   - CTRL+C to stop the program entirely 
   

## Do not worry about the folder "testground", it is just for testing making sure this works but feel free tinker with it if you know what you're doing.

## Warnings!!

Do not `Go back one page` or you will break the program

## Credits

I took inspiration from Co-authors SiakTzu, Hocky, Dennis, Galang and sl1ckthread on github. I have only modified their codes to work better on MacOS. 

## Contact

For further assistance, you know how to find me :3.
