from django.shortcuts import render,HttpResponse

import cv2
import argparse
import sys
import numpy as np

# Create your views here.

def home(request):
	if request.method == "GET":
		return render(request,'accounts/login.html')
	elif request.method== "POST":
		attachment = request.FILES['video-opticalflow']
	keep_processing = True
	def draw_flow(img, flow, step=8):
	    h, w = img.shape[:2]
	    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
	    fx, fy = flow[y,x].T
	    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
	    lines = np.int32(lines + 0.5)
	    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	    cv2.polylines(vis, lines, 0, (0, 255, 0))
	    for (x1, y1), (x2, y2) in lines:
	        cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
	    return vis
	    out.write(vis)
	cap=cv2.VideoCapture()
	frame_width = int(cap.get(3))
	frame_height = int(cap.get(4))
	fourcc = cv2.VideoWriter_fourcc('M','J','P','G') 
	out = cv2.VideoWriter('C:\\Users\\user\\Desktop\\videos\\output1.mp4',fourcc, 10, (frame_width,frame_height)) 
	windowName = "Dense Optic Flow" # window name
	if ((cap.open(str("C:\\Users\\user\\Desktop\\videos\\"+str(attachment))))):
	    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
	    if (cap.isOpened()):
	        ret, frame = cap.read()
	        if (True):
	            frame = cv2.resize(frame, (0, 0), fx=1.0, fy=1.0)
	    prevgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	    while (keep_processing):

	        if (cap.isOpened):
	            ret, frame = cap.read()
	            if (ret == 0):
	                keep_processing = False
	                continue
	            if (True):
	                frame = cv2.resize(frame, (0, 0), fx=1.0, fy=1.0)
	        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	        flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
	        prevgray = gray
	        out.write(draw_flow(gray,flow))
	        cv2.imshow(windowName, draw_flow(gray, flow))
	        


	                  
	        key = cv2.waitKey(40) & 0xFF
	        if (key == ord('x')):
	            keep_processing = False
	        elif (key == ord('f')):
	        	cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	cv2.destroyAllWindows()
	out.release()
	return render(request, 'accounts/success.html')

	#else:
	    #print("No video file specified or camera connected.")