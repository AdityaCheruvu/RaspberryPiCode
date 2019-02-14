import cv2
import os

def blur_detection(img_path):
		for file_name in os.listdir(img_path):

				f_name=os.path.join(img_path,file_name)

				if(f_name.endswith(("jpg","JPG","png"))):

					img=cv2.imread(f_name)

					if((cv2.Laplacian(img,cv2.CV_64F).var())<110):
						print("removing file ",f_name)	
						os.remove(f_name)
						
		
			
		



