# 졸업작품 - 얼굴 인식을 기반한 초상권 침해 방지 시스템 <br/>

:book: 졸업 작품 <br/>
: 얼굴 인식을 기반한 초상권 침해 방지 시스템 <br/>

:round_pushpin: 개발 기간 : 2022.08 ~ 2023.05 10개월 <br/> 
:round_pushpin: 플랫폼 : App <br/>
:round_pushpin: 개발 인원 : 2명 <br/>
:round_pushpin: 담당 역할 : 얼굴 인식(기여도 80%), 서비스 기획 및 방향성 설정(기여도 90%), 안드로이드(기여도 40%) <br/>

[Development environment] <br/>
:round_pushpin: 언어 : Python 3.6.8, Java 11.0.1 <br/>
:round_pushpin: DB : FireBase storage <br/>
:round_pushpin: IDE : Raspberry Pi 3B+, Android Studio <br/>

:round_pushpin: [Description] <br/>
Project Overview : 개인 방송 플랫폼의 증가로 인해 실시간 방송을 진행하는 과정에서 지나가는 시민들의 얼굴이 무차별적으로 노출이 되어 초상권을 침해하는 일이 빈번하게 발생하고 국민 청원뿐만 아니라 피해 신고 접수 또한 급격히 늘고 있다. 이와 같은 문제를 해결하기 위해 얼굴 인식을 기반한 초상권 침해 방지 시스템을 제작하기로 하였다. <br/>

:round_pushpin: [Algorithm] <br/>
![image](https://user-images.githubusercontent.com/102573192/210356161-e78fed26-8a45-40cb-9fe3-fac1acb6b48f.png) <br/> 
![image](https://user-images.githubusercontent.com/102573192/215275548-01bbe2d8-3778-4426-ba26-106ee113a3ea.png) <br/> 
<br/> 

1️⃣ 카메라로 실시간 스트리밍을 한다. <br/>
2️⃣ 이때 학습자는 사전에 haar 알고리즘을 통해 얼굴 등록 과정을 거치고 DB에 저장한다.  <br/>
3️⃣ 실시간 방송 중 일반인의 얼굴이 감지될 경우 adaboost 알고리즘으로 DB에 저장된 학습자의 얼굴과 비교한다. <br/>
4️⃣ 비교 기준은 기존 설정한 임계값 미만일 경우 학습자가 아닌 것으로 판단한다. <br/>
:five: mosaic 처리 알고리즘 기술로 학습자가 아닌 사람은 모자이크 처리를 하여 초상권을 보호한다.<br/>

<br/>

:round_pushpin: [Architecture] <br/>
![image](https://github.com/kyounggseo/real-time-face/assets/102573192/07878a69-34e1-4563-9e50-d639467a6f89) <br/>
1️⃣ 라즈베리파이 카메라를 통해 실시간 스트리밍을 한다. <br/>
2️⃣ 학습자가 이닌 일반인의 얼굴이 감지될 경우 초상권 보호를 위해 모자이크 처리 알고리즘 과정을 거친다. <br/>
3️⃣ 실시간 스트리밍을 보는 시청자는 실시간으로 일반인의 얼굴이 모자이크 된 영상을 보게 된다. <br/>
<br/>

✏️ case1 : 일반인 <br/>
![image](https://user-images.githubusercontent.com/102573192/210356297-37bff7e5-de71-4aa0-966e-c9e7660e455c.png) <br/>
✅ 학습자가 아닌 일반인으로 인식 될 경우 모자이크 처리를 함으로써 초상권 보호를 할 수 있다. <br/>
<br/>

✏️ case2 학습자 <br/>
![image](https://github.com/kyounggseo/real-time-face/assets/102573192/b7258bad-fec2-42dc-9b71-60d96ce24290) <br/>
✅ 학습자로 인식 될 경우 학습자 자신의 이름이 나오면서 모자이크 처리를 하지 않는다. <br/>
<br/>

:round_pushpin: [Result] <br/>
![image](https://github.com/kyounggseo/real-time-face/assets/102573192/9ebc3fc3-4106-4c21-b6c0-16da77fb7979) <br/>
<br/>

✅ 학습자가 아닌 일반인으로 인식 될 경우 모자이크 처리를 함으로써 초상권 보호를 할 수 있다. <br/>
✅ 학습자로 인식 될 경우 학습자 본인의 이름이 나오면서 모자이크 처리를 하지 않는다.<br/>
✅ 실시간으로 방송 플랫폼을 시청하는 시청자는 일반인의 초상권이 모자이크 처리 된 영상을 볼 수 있다.<br/>
