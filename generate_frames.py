import cv2
import os
cap = cv2.VideoCapture('./video_data/video1.mp4')

filelist = [ f for f in os.listdir("./frames/") if f.endswith(".jpg") ]
for f in filelist:
    os.remove('./frames/'+f)



count = 0
try :
	while cap.isOpened():
	    ret,frame = cap.read()
	    cv2.imshow('window-name',frame)
	    cv2.imwrite("./frames/frame%d.jpg" % count, frame)
	    count = count + 1
	    if cv2.waitKey(10) & 0xFF == ord('q'):
	        break
	cap.release()
	cap.destroyAllWindows()
except :
	pass


fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
print 'Frames Per Second :',fps
with open('videoinfo.txt' , 'w') as f :
	f.write('No. of Frames :%s'%str(count))
	f.write('\nFPS :%s'%str(fps))

