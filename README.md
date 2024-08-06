# EpakSIAK

**WELCOME** 

You might be wonderin what is "EpakSIAK" and how you can use it to hopefully win the SIAK war. Essentially "EpakSIAK" can help you constantly refresh and choose your classes for you increasing your chance of winning. EpakSIAK is specifically designed to run on MacOS. EpakSIAK can run in windows/linux too however i much recommend you check out sl1ckthreads's SiakJover bot as that is simpler and more geared towards windows/linux.

## Setup Instructions

### 1. Prerequisites

   - **Open Terminal**: Open command prompt or terminal depending on your operating system

   - **Get Homebrew**: This is MacOS specific so just skip if you're using windows. For all you MacOS users however, copy and paste the command below into your terminal. You might need to put in your password, don't worry this is standard practice. You might also need to restart your device after installing so do so real quick.
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
     
   - **Get Python**: Obviously since EpakSIAK runs on Python, you need to have that installed on your device. Open cmd (Windows) or terminal and install python using:
```
brew install python
```

   - **Install TKinter**: If you're not using MacOS, don't worry about this since it's generally already installed on the windows/linux version of Python (although doing this step just to make sure it is up-to-date is still a good idea). For all you mac users however, use:
```
brew install python-tk
```
   - **Download EpakSIAK**: I recommend cloning this repisotory using git (for this to work you need to have git preinstalled https://git-scm.com/downloads, download the one that corresponds to your OS). You can clone by using this command below. Alternatively, you can download the ZIP directly but for instructions sake just use git.
```
git clone https://github.com/rudysworld/EpakSIAK.git
```

   - **Install chromedriver**: If you're on MacOS and If you're using this near the time as of me writing this (3 August 2024) don't worry about this since i have already installed it for you in this folder and it should still be up to date. However if you're not using MacOS or if you're using this in the future, replace the one in this folder with a chromedriver that corresponds to your current OS and version of Google Chrome.

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
   

## Warnings!!

Do not `Go back one page` or you will break the program

## Credits

I took inspiration from Co-authors SiakTzu, Hocky, Dennis, Galang and sl1ckthread on github. I have only modified their codes to work better on MacOS. 

## Contact

For further assistance, you know how to find me :3.
