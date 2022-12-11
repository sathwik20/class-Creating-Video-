import cv2

vid=cv2.VideoCapture(0)

if(vid.isOpened()==False):
    print('unable to read the feed')

height=int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)     

width=int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps=int(vid.get(cv2.CAP_PROP_FPS))
print(fps)
out=cv2.VideoWriter('myself.mp4',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))

while(True):
    #Capture the video frame by frame
    ret,frame=vid.read()
    cv2.imshow('webcame',frame)
    out.write(frame)
    if cv2.waitkey(25)==32:
        break

vid.release()
out.release()        
cv2.destroyAllWindows()
