import os, shutil, time

# A function to organize your files (file organiztaion - data cleaning - sys maintenance)
def OrganizeFiles(TargetDir):
    # Step 1: That Ensures that the directory path ends with a slash if not it adds a forward slash
    if not TargetDir.endswith('/'):
        TargetDir += '/'
    # Step 2: Iterate over all files and directories in the specified directory needed
    # Step 2.1: Check if the item is a file
    for item in os.listdir(TargetDir):
        ItemPath = os.path.join(TargetDir, item)
        if os.path.isfile(ItemPath):
            # Step 2.1.1: Extract file extension and removing the dot from the extension
            # Step 2.1.2: Create directory if it doesn't exist
            # Step 2.1.3: Finaaly, Moving the file to corresponding directory
            _, extension = os.path.splitext(item)
            extension = extension[1:]
            if not os.path.exists(TargetDir + extension):
                os.makedirs(TargetDir + extension)
            shutil.move(ItemPath, TargetDir + extension + '/' + item)

def RunTaskAutomation():
    TargetDir = input("Enter the path to your direcotry: ")
    OrganizeFiles(TargetDir)
    time.sleep(1.5)
    print("Files organized successfully!, Go Check on your partition.")
RunTaskAutomation()