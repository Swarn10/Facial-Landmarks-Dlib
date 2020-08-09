# Facial-Landmarks-Dlib
Detection of facial landmarks and their positions using dlib library for emotion and mood detection.  


1) The program detects the facial landmarks like nose, mouth, eyes etc. and returns their co-ordinates. 
2) It further plots the returned co-ordinates on the input image to generate the output image. 
3) This program can serve as the basis for more powerful applications like real-time mood/emotion detection. 


Note 1 :- This was developed by me during Inter-Hall Open-Soft Competition as an integral member. 

Note 2 :- 
For hassle free operation we need the following libraries : 

1) Installing dlib requires certain pre-requisites such as CMake,Boost and X11 . They can be installed by running the following 
           
           $ sudo apt-get install build-essential cmake
           $ sudo apt-get install libgtk-3-dev
           $ sudo apt-get install libboost-all-dev 
   
2) Install dlib by running the following on terminal 
           $ pip3 install dlib 
           
3) Install opencv by running the following on terminal 
           $ sudo apt-get install python3-opencv

4) Keep the following pre-trained models for facial-features detection in the directory where you have extract_face_features.py 
   Download it from https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/shape_predictor_68_face_landmarks.dat
