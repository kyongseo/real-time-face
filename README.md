# 졸업작품 - 얼굴 인식을 기반한 초상권 침해 방지 시스템 <br/>

:book: 졸업 작품 <br/>
: 얼굴 인식을 기반한 초상권 침해 방지 시스템 <br/>

:round_pushpin: 개발 기간 : 2022.11 ~ 2023.04 6개월 <br/> 
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
1️⃣ 카메라로 사람을 인식한다.<br/>
2️⃣ haar 알고리즘으로 얼굴을 인식한다.  <br/>
3️⃣ adaboost 알고리즘으로 사전에 학습된 학습자인지 아닌지 구별한다. (임계값 미만일 경우 학습자가 아닌 것으로 판단함) <br/>
4️⃣ mosaic 기술로 학습자가 아닌 사람은 모자이크 처리를 한다.<br/>
<br/>
✏️ case1 : Ordinary person <br/>
![image](https://user-images.githubusercontent.com/102573192/210356297-37bff7e5-de71-4aa0-966e-c9e7660e455c.png) <br/>
✅ 학습자가 아닌 일반인으로 인식 될 경우 모자이크 처리를 함으로써 초상권 보호를 할 수 있다. <br/>

✏️ case2 : learner <br/>
✅ 자신의 이름이 나오면서 학습자로 인식한다. <br/>
![image](https://github.com/kyounggseo/real-time-face/assets/102573192/236f1b56-5e35-49b3-bdb8-5442970bcfef)

:round_pushpin: [Result] <br/>
![image](https://github.com/kyounggseo/real-time-face/assets/102573192/0f0e04d4-1056-4c51-92be-235edbb46b93) <br/>
![image](https://github.com/kyounggseo/real-time-face/assets/102573192/3804041c-bacb-487a-9235-a4f23880b93f)<br/>

