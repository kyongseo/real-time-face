import cv2
import numpy as np
import torch
from torch.utils.data import DataLoader
from time import time
import subprocess
import ffmpeg

waybill_weight = "/content/waybill_v1.2_r45.pt"
plate_weight="/content/plate.pt"
combined_weight="/content/all_combined_v2.3.2_flip.pt"


base_url = "rtmp://3.34.97.138/"

DataLoader.num_workers=0

class MosaicObject:

    # 초기화
    def __init__(self):
        self.model=self.load_model()
        self.classes=self.model.names

    # 모델 설정
    def load_model(self):
        model=torch.hub.load('ultralytics/yolov5', 'custom', path=waybill_weight)
        # model = torch.hub.load('ultralytics/yolov5','yolov5s')
        return model

    # 프레임별로 inference 진행 -> 인식한 label 및 정보 반환
    def score_frame(self, frame):
        frame=[frame]
        results=self.model(frame)
        labels,cord = results.xyxyn[0][:,-1].cpu().numpy(), results.xyxyn[0][:,:-1].cpu().numpy()
        return labels,cord

    # 클래스 값에 해당하는 label명 (string) 반환
    def class_to_label(self,x):
        return self.classes[int(x)]

    # 모자이크
    def mosaic_frame(self,results,frame):
        labels,cord=results
        n=len(labels)

        x_shape,y_shape=frame.shape[1],frame.shape[0]   # x_shape = 높이, y_shape = 너비

        # 검출된 객체 수만큼 돌며, 모자이크 처리
        for i in range(n):
            row=cord[i]     # row : xmin, ymin, xmax, ymax, confidence, class, name 
            if row[4] >= 0.6 :      # confidence 하한값 설정
                left=int(row[0]*x_shape)
                top=int(row[1]*y_shape)
                right=int(row[2]*x_shape)
                bottom=int(row[3]*y_shape)

                mosaic_part=frame[top:bottom,left:right]    # 모자이크 범위 설정
                mosaic_part=cv2.blur(mosaic_part,(50,50))   

                frame[top:bottom,left:right]=mosaic_part    # 해당 범위 모자이크처리한걸 원본에 덮어쓰기

        return frame


def run():
    
  rtmp_in_url = base_url + "live/test"
  rtmp_out_url = base_url + "live-out"
  cap=cv2.VideoCapture(rtmp_in_url)

  fps = int(cap.get(cv2.CAP_PROP_FPS))
  width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


  mosaicObject = MosaicObject();
  mosaicObject.__init__

  fps = int(cap.get(cv2.CAP_PROP_FPS))
  width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

  command = ['ffmpeg',
           '-y',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', "{}x{}".format(width, height),
           '-r', str(fps),
           '-i', '-',
           '-c:v', 'libx264',
           '-pix_fmt', 'yuv420p',
           '-preset', 'ultrafast',
           '-f', 'flv',
           rtmp_out_url]
  
  p=subprocess.Popen(command,stdin=subprocess.PIPE)

  while cap.isOpened():
      start_time = time()

      status, frame = cap.read()
      if not status : 
        print('can not read!')
        break

      results=mosaicObject.score_frame(frame)
      frame=mosaicObject.mosaic_frame(results,frame)

      # rtmp 서버로 push
      p.stdin.write(frame.tobytes())

      end_time=time()
      fps=1/np.round(end_time-start_time,3)
      print(f"FPS = {fps}")

  cap.release()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  run()
