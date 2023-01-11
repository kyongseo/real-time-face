# 졸업작품 - 얼굴 인식을 기반한 초상권 침해 방지 시스템 <br/>

:book: 졸업 작품 <br/>
: 얼굴 인식을 기반한 초상권 침해 방지 시스템 <br/>

:round_pushpin: 개발 기간 : 2022.11 ~ 2023.04 6개월 <br/> 
:round_pushpin: 플랫폼 : App <br/>
:round_pushpin: 개발 인원 : 2명 <br/>
:round_pushpin: 담당 역할 : 얼굴 인식(기여도 80%), 서비스 기획 및 방향성 설정(기여도 90%) <br/>

[Development environment] <br/>
:round_pushpin: 언어 : Python 3.6.8, Java 11.0.1 <br/>
:round_pushpin: DB : FireBase storage <br/>
:round_pushpin: IDE : Raspberry Pi, Android Studio <br/>

:round_pushpin: [Description] <br/>
Project Overview : 개인 방송 플랫폼의 증가로 인해 실시간 방송을 진행하는 과정에서 지나가는 시민들의 얼굴이 무차별적으로 노출이 되어 초상권을 침해하는 일이 빈번하게 발생하고 국민 청원뿐만 아니라 피해 신고 접수 또한 급격히 늘고 있다. 이와 같은 문제를 해결하기 위해 얼굴 인식을 기반한 초상권 침해 방지 시스템을 제작하기로 하였다. <br/>

:round_pushpin: [Algorithm] <br/>
![image](https://user-images.githubusercontent.com/102573192/210356161-e78fed26-8a45-40cb-9fe3-fac1acb6b48f.png) <br/> 
1️⃣ 학습자 얼굴 인식 - 총 50장의 학습자 사진 등록 <br/>
2️⃣ 임계값 미만일 경우 일반인으로 인식 => 초상권 방지를 위해 모자이크 처리 <br/>

✏️ case1 : Ordinary person <br/>
![image](https://user-images.githubusercontent.com/102573192/210356297-37bff7e5-de71-4aa0-966e-c9e7660e455c.png) <br/>
✅ 학습자가 아닌 일반인으로 인식 될 경우 모자이크 처리를 함으로써 초상권 보호를 할 수 있다. <br/>

✏️ case2 : learner <br/>
✅ 자신의 이름이 나오면서 학습자로 인식한다. <br/>
