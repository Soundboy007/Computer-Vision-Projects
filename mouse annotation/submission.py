import cv2

def drawBox(action, x, y, flags, userdata):
    global point1, point2
    
    if action == cv2.EVENT_LBUTTONDOWN:
        point1 = [(x,y)]
        
    elif action == cv2.EVENT_LBUTTONUP:
        point2 = [(x,y)]        
        cv2.rectangle(source, point1[0], point2[0], (255,255,255), thickness=2, lineType=cv2.LINE_8)
        imgroi = source.copy()
        height = point1[0][1] - point2[0][1] 
        width = point2[0][0] - point1[0][0]
        #print(height, width)
        #print(point1, point2)
        
        if height<0 and width>0:
            imgroi = imgroi[point1[0][1]:point1[0][1]-height,point1[0][0]:point1[0][0]+width]
            #v2.imshow('imgroi',imgroi)
            cv2.imwrite('cropped_image.jpg',imgroi)
            
        elif height<0 and width<0:
            imgroi = imgroi[point1[0][1]:point1[0][1]-height,point2[0][0]:point2[0][0]-width]
            #cv2.imshow('imgroi',imgroi)
            cv2.imwrite('cropped_image.jpg',imgroi)
          
        elif height>0 and width>0:
            imgroi = imgroi[point2[0][1]:point2[0][1]+height,point1[0][0]:point1[0][0]+width]
            #cv2.imshow('imgroi',imgroi)
            cv2.imwrite('cropped_image.jpg',imgroi)
            
        elif height>0 and width<0:
            imgroi = imgroi[point2[0][1]:point2[0][1]+height,point2[0][0]:point2[0][0]-width]
            #cv2.imshow('imgroi',imgroi)
            cv2.imwrite('cropped_image.jpg',imgroi)
                       
source = cv2.imread('sample.jpg')
dummy = source.copy()
cv2.namedWindow('window')
k = (cv2.waitKey(10) & 0XFF)

cv2.setMouseCallback('window', drawBox)
while k!=ord('q'):
    cv2.putText(source,'''Drag mouse to crop. 'q': quit, 'c': clear''', (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255),2)    
    cv2.imshow('window', source)
    k = cv2.waitKey(10) & 0xFF
    if k == ord('c'):
        source = dummy.copy()
        
cv2.destroyAllWindows()