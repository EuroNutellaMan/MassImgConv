from PIL import Image, ImageFilter
from PyQt6.QtWidgets import QApplication, QFileDialog, QMessageBox
import os
from tqdm import tqdm
import sys

app = QApplication(sys.argv)

def quit_program():
    app.exit()

# Create a PyQt6 window to select the input files
file_filter = 'Image files (*.jpg *.jpeg *.webp *.png)'
file_dialog = QFileDialog.getOpenFileNames(
    caption='Select image files',
    directory='/home/lorenzob/',
    filter=file_filter,
    initialFilter='Image files (*.jpg *.jpeg *.webp *.png)'
)
for filepath in file_dialog[0:-1]:
    filepaths = filepath

# Show a dialog box to ask if the user wants to scale the images
scaler = QMessageBox.question(None, "Scale Images", "Do you want to scale the images?")
if scaler == 16384:
    scale_img = 'Yes'
else:
    scale_img = 'No'

# Show a confirmation dialog box to ask if the user wants to delete the original file
ogdeleter = QMessageBox.question(None, "Delete Original", "Do you want to delete the original files?")
if ogdeleter == 16384:
    ogdel = 'Yes'
else:
    ogdel = 'No'

# Initialize the progress bar
total_files = len(filepaths)
progress_bar = tqdm(total=total_files, unit='file(s)', desc='Converting')

# Loop through all the selected files
for filepath in filepaths:
    # Open the JPEG file using Pillow
    img = Image.open(filepath)
    if scale_img == 'Yes':
        # Determine the maximum dimension (width or height) to be scaled to 512 pixels
        width, height = img.size
        if max(width, height) > 512:
            if width > height:
                new_width = 512
                new_height = int((height / width) * new_width)
            else:
                new_height = 512
                new_width = int((width / height) * new_height)

            # Scale the image while maintaining the aspect ratio
            img = img.resize((new_width, new_height), Image.LANCZOS)

    # Change the file extension from .jpg to .png
    if '.jpg' in filepath:
        new_filepath = filepath.replace('.jpg', '.png')
    elif '.jpeg' in filepath:
        new_filepath = filepath.replace('.jpeg', '.png')
    elif '.webp' in filepath:
        new_filepath = filepath.replace('.webp', '.png')

    # Save the converted file in the same directory
    img.save(new_filepath)

    # Close the Pillow image object
    img.close()
    
    # Deletes original files if specified
    if ogdel == 'Yes':
        os.remove(filepath)
    
    # Update the progress bar
    progress_bar.update(1)

# Close the progress bar
progress_bar.close()

# Create a new window for the "Finished!" message and OK button
closer = QMessageBox.information(None, "Finished!", "Operation completed!")
if closer:
    quit_program()