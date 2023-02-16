import csv
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
plt.rc('font', size=7)
f=open('C:\\Users\\A18\\ezwork\\day32\\starbucks_suwon.csv')
data = csv.reader(f) # csv파일은 콤마로 구분
next(data) # 타이틀 안보이게 함
dong = ["영통동",
    "원천동",
    "망포동",
    "신동",
    "서둔동",
    "세류동",
    "권선동",
    "평동",
    "금곡동",
    "송죽동",
    "정자동",
    "율천동",
    "파장동",
    "연무동",
    "인계동",
    "우만동",
    "매산동"
    ]
spop =[]
for row in data :
    if (row[4] != "") :
        spop.append(float(row[4]))
plt.title("수원지역 스타벅스 점포당 인구수") #큰제목
plt.xlabel("행정동")  #x축 제목
plt.ylabel("점포당 인구수") #y축제목
plt.plot(dong, spop)
plt.scatter(dong, spop)
plt.show()
