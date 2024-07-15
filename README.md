# Build Instructions

## Requirements

- Python installed on your system
- Command line access (cmd)

## Steps to Build the Project

1. **Open the Command Line (cmd)**

   Open the command line on your system. You can do this by searching for "cmd" in the Start menu and selecting "Command Prompt".

2. **Install PyInstaller**

   Make sure you have PyInstaller installed. You can install it by running the following command:

   ```sh
   pip install pyinstaller
   ```
3. Navigate to Your Project Folder

Open the command line in the folder where your project is located. You can use the cd command to navigate to the correct folder. For example:

```sh
cd C:\path\to\your\project
```
4. Run PyInstaller

Run the following command to build your project with PyInstaller:

```sh
pyinstaller --onefile --noconsole script.py
```
Make sure to replace script.py with the name of your main Python script.

5. Check the Build

After PyInstaller finishes, you should find your executable file in the dist folder within your project directory.

## Notes
- The --onefile option packages everything into a single executable file.
- The --noconsole option prevents a console window from opening when you run the file.
- You can add an icon to your executable using the --icon=your_icon.ico option.
## Run the Compiled File
Once you have the executable file in the dist folder, you can run it by double-clicking it or from the command line:

```sh
cd dist
furry.exe
```
