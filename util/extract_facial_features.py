import numpy as np 
import pandas as pd 
import cv2 
import dlib 


PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat" 
detector = dlib.get_frontal_face_detector() 
predictor = dlib.shape_predictor(PREDICTOR_PATH) 



def get_features(im) :   # This function detects the bounding-box for the face and then creates a list of 68 coordinates ,i.e, "features" and using that creates a dictionary with
						             # facial landmarks as keys and their list of coordinates as values 	
	
	rectangle = detector(im,1) 
	
	if len(rectangle) == 0 : 
		print("No faces detected !!!") 
		features = [] 
		features_dict = {} 
		return (features,features_dict) 

	features = [(p.x,p.y) for p in predictor(im,rectangle[0]).parts()]  
	features_dict = {"Jaw":[],"Left eyebrow":[], "Right eyebrow":[], "Nose":[], "Left eye" : [], "Right eye": [], "Mouth" : []} 
	
	for i in range(68) : 
		if i < 17 : 
			features_dict["Jaw"].append(features[i]) 
		elif i < 22 : 
			features_dict["Left eyebrow"].append(features[i]) 
		elif i < 27 : 
			features_dict["Right eyebrow"].append(features[i]) 
		elif i < 36 : 
			features_dict["Nose"].append(features[i]) 
		elif i < 42 : 
			features_dict["Left eye"].append(features[i]) 
		elif i < 48 : 
			features_dict["Right eye"].append(features[i]) 
		else : 
			features_dict["Mouth"].append(features[i]) 
	
	return (features_dict,features)   


def put_features(im, features) :  # This function plots those 68 points as cirlces on the original image 
	
	im = im.copy() 
	
	for point in features :  
		cv2.circle(im,point,3,color=(0,255,255)) 

	return im 




if __name__ == '__main__' : 
	image = cv2.imread('no_face.jpg') 
	features_dict,features = get_features(image) 

	print(features_dict)
	print("\n")
	print(features)  

	if len(features) != 0 : 
		img_with_features = put_features(image,features) 
		cv2.imwrite('Result4.jpg',img_with_features) 