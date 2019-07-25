from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
import os
import sys
from PIL import ImageTk, Image
import cv2
import Binary, Morphology, BoundaryExtraction, Skeletonize
from datetime import datetime

#TODO: 
#add descriptions for each morphological operation
#Add last func on binary, skeletization 
#add the otsu's algorithm and greyscale algorithm
#add functions that are ran on greyscale images


inputImage = []
global label
global finalLabel
global description
imageTypeValue = 0
funcType = 0


def getImage(self):
    curDir = os.getcwd()
    imageLocation = filedialog.askopenfilename(
        initialdir = curDir, title = "Select file", 
        filetypes = (("jpeg files","*.jpg *.jpeg"),("png files","*.png")))

    #this makes the input image into a matrix
    global inputImage
    inputImage = cv2.imread(imageLocation, 0)
    global greyOrBinaryImage
    greyOrBinaryImage = makeGreyOrBinary()

    #resize image and display in gui
    binaryImageName = curDir + "/inputImage.jpg"
    cv2.imwrite(binaryImageName, greyOrBinaryImage)
    im_temp = Image.open(binaryImageName)
    im_temp = im_temp.resize((250, 250), Image.ANTIALIAS)
    im_temp.save("ArtWrk.ppm", "ppm")
    img = ImageTk.PhotoImage(file ="ArtWrk.ppm")
    label = tk.Label(root, image = img)
    label.grid(row = 10, columnspan = 6)
    label.image = img

    return 


def getImageType():
    global imageTypeValue
    imageTypeValue = binaryGreyValue.get()    
    return




def getFunctionType():
    global funcType
    funcType = functionTypeValue.get()
    return




def makeGreyOrBinary():
    if imageTypeValue == 2: #greyscale (Otsu's)
        print("greyscale")
    elif imageTypeValue == 1:
        binaryObj = Binary.Binary()
        histogram = binaryObj.compute_histogram(inputImage)
        optThreshold = binaryObj.find_optimal_threshold(histogram, inputImage)
        returnImage = binaryObj.binarize(inputImage, optThreshold)

    return returnImage


def runFunction(updatedImage):
    morphologyObj = Morphology.Morphology()
    boundaryExtractObj = BoundaryExtraction.BoundaryExtraction()
    skelObj = Skeletonize.Skeletonize()
    global description
    if funcType == 1:
        # Erosion
        description = "                      Erosion"
        finalImage = morphologyObj.erosion(updatedImage)
    elif funcType == 2:
        # Dilation
        description = "                     Dilation"
        finalImage = morphologyObj.dilate(updatedImage)
    elif funcType == 3:
        # Opening
        description = "                    Opening"
        finalImage = morphologyObj.open(updatedImage)
    elif funcType == 4:
        # Closing
        description = "                    Closing"
        finalImage = morphologyObj.close(updatedImage)
    elif funcType == 5:
        # Open-Close
        description = "                 Open-Close"
        finalImage = morphologyObj.open_close(updatedImage)
    elif funcType == 6:
        # Close-Open
        description = "                 Close-Open"
        finalImage = morphologyObj.close_open(updatedImage)
    elif funcType == 7:
        # Skeletanization
        description = "        Skeletanization"
        finalImage = skelObj.skeletonize(updatedImage)
    elif funcType == 8:
        # Boundary Extraction
        description = "Boundary Extraction"
        erodedImage = boundaryExtractObj.erodeImage(updatedImage)
        finalImage = boundaryExtractObj.subtractImages(erodedImage, updatedImage)

    return finalImage



def processImage(self):

    if(imageTypeValue == 0 or funcType == 0 or inputImage == []):
        messagebox.showerror("Error", "You didn't fill out all the options!")
        return

    greyOrBinaryImage = makeGreyOrBinary()
    prcoessedImage = runFunction(greyOrBinaryImage)

    Label(root, text=description).grid(row=7, column=7)
    curDir = os.getcwd()

    outputImageName = curDir + "/curImage.jpg"
    cv2.imwrite(outputImageName, prcoessedImage)

    #resize and display processed image
    im2 = Image.open(outputImageName)
    im2 = im2.resize((250, 250), Image.ANTIALIAS)
    im2.save("ArtWrk1.ppm", "ppm")
    finalImage = ImageTk.PhotoImage(file = "ArtWrk1.ppm")
    finalLabel = tk.Label(root, image = finalImage)
    finalLabel.grid(row = 10, column = 7, columnspan = 6)
    finalLabel.image = finalImage
    return




root = Tk()


Label(root, text= "Upload a binary or greyscale image").grid(row=0, columnspan = 3, sticky=W)
root.title("Image Morphology")
root.geometry("700x500")


Label(root, text= "Upload a binary or greyscale image").grid(row=0, columnspan = 3, sticky=W)
f1 = tk.Frame(root, height = 250, width = 250 , bg = 'white')
f1.grid(row = 10, columnspan = 6)
f2 = tk.Frame(root, height = 250, width = 250 , bg = 'white')
f2.grid(row = 10, column = 7, columnspan = 6)

Label(root, text= "Choose an image type:").grid(row=1, columnspan = 3, sticky=W)
binaryGreyValue = IntVar()
#radiobuttons were set with values 1 for binary, and 2 for greyscale, stored in var v
Radiobutton(root, text = "Binary", value = 1, variable = binaryGreyValue, command = getImageType).grid(row = 2, column = 0, sticky = W)
Radiobutton(root, text = "Greyscale", value = 2, variable = binaryGreyValue, command = getImageType).grid(row = 2, column = 1, sticky = W)


Label(root, text= "Choose an Image Morphology Method").grid(row=3, columnspan = 3, sticky=W)
functionTypeValue = IntVar()
Radiobutton(root, text = "Erosion", value = 1, variable = functionTypeValue, command = getFunctionType).grid(row = 4, column = 0, sticky = W)
Radiobutton(root, text = "Dilation", value = 2, variable = functionTypeValue, command = getFunctionType).grid(row=5, column=0, sticky = W)
Radiobutton(root, text = "Opening", value = 3, variable = functionTypeValue, command = getFunctionType).grid(row = 4, column = 1, sticky = W)
Radiobutton(root, text = "Closing", value = 4, variable = functionTypeValue, command = getFunctionType).grid(row = 5, column = 1, sticky = W)
Radiobutton(root, text = "Open-Close", value = 5, variable = functionTypeValue, command = getFunctionType).grid(row = 4, column = 2, sticky = W)
Radiobutton(root, text = "Close-Open", value = 6, variable = functionTypeValue, command = getFunctionType).grid(row = 5, column = 2, sticky = W)
Radiobutton(root, text = "Skeletinization", value = 7, variable = functionTypeValue, command = getFunctionType).grid(row = 4, column = 3, sticky = W)
Radiobutton(root, text = "Boundary Extraction", value = 8, variable = functionTypeValue, command = getFunctionType).grid(row = 5, column = 3, sticky = W)



loadImageButton = Button(root, text= "Upload Image")
loadImageButton.bind("<Button-1>", getImage)
loadImageButton.grid(row=6, column=0)


processImageButton = Button(root, text = "Process")
processImageButton.bind("<Button-1>", processImage)
processImageButton.grid(row = 100, column = 0, sticky = W)




root.mainloop()
