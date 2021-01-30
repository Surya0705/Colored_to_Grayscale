import cv2 # Importing OpenCV.
from tkinter import filedialog # Importing tkinter filedialog for choosing image.

Path = filedialog.askopenfilename(title="Select Image") # Giving the Path.
Img = cv2.imread(Path) # Defining the Image.
Grayed_Img = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY) # Applying the filter.

cv2.imshow("Original Image", Img) # Displaying the Original Image.
cv2.imshow("Grayed Image", Grayed_Img) # Displaying the Grayed Image.
cv2.waitKey(0) 
cv2.destroyAllWindows()