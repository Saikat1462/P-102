from os import name
import cv2
import dropbox
import time
import random
import os

start_time=time.time()
def take_snapshot():
    number=random.randint(0,1000)
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshot taking")
    VideoCaptureobject.release()
    cv2.destroyAllWindows()
#take_snapshot()

def upload_file(img_name):
    access_token="sl.A73YdEr5FY0z7bmgiUv1DcvGz6w-Rm_P0Ydd2RLiSbMl5V2nWRRIAov2SM-Eogr-Gs0vgLVO70CzW6uH-GNpwGGM3d54rTKAT1YwsfFpTugaw7HuTVBPlusgKjOUS4uY-RgzmeA"
    file=img_name
    file_from="/WhiteHat Junior/Class 102"
    file_to="/newFolder1"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    os.path.isfile(file_from)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded")
def main():
    while(True):
        if((time.time() -start_time)>=10):  
            name=take_snapshot()
            upload_file(name)
main()