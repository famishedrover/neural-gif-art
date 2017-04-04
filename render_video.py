import os 
import cv2

filelist = [ f for f in os.listdir("./output") if f.endswith(".avi") ]
for f in filelist:
    os.remove(f)




with open('videoinfo.txt','r') as f :
	x= f.read()
x = x.replace('No. of Frames :','').replace('FPS :','')
x = x.split('\n')
print x
len_frames = int(x[0]) 
fps = int(float(x[1]))
print fps

lim =  len_frames
path = './frames/'
im1 = cv2.imread(path +'frame'+str(0)+'.jpg')

height , width , layers = im1.shape
video = cv2.VideoWriter('./output/video.avi' , -1 , fps ,(width,height))
video.write(im1)

for ix in range (1,lim) :
	im = cv2.imread(path +'frame'+str(ix)+'.jpg')
	video.write(im)

cv2.destroyAllWindows()
video.release()
