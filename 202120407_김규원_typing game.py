import random         
import time               
import numpy as np
import pickle
import os
 
li=[0,0,0,0,0,0,0,0,0,0]
w=["Faith without deeds is useless.","Forgiveness is better than revenge.",
   "We never know the worth of water till the well is dry.","Love your neighbor as yourself.",
   "Education is the best provision for old age.","The most beautiful thing in the world is, of course, the world itself.",
   "All fortune is to be conquered by bearing it.","Think like a man of action and act like man of thought.","Courage is very important. Like a muscle, it is strengthened by use.",
   "A man that hath no virtue in himself, ever envieth virtue in others.","Error is the discipline through which we advance.",
   "Books are ships which pass through the vast seas of time.","United we stand, divided we fall.","Let thy speech be short, comprehending much in few words.",
   "Better is to bow than break.","Good fences makes good neighbors."
   
   
   ]
v=['행함이 없는 믿음은 쓸모가 없다.',"용서는 복수보다 낫다.",
   "우물이 마르기까지는 물의 가치를 모른다.","네 이웃을 네 몸처럼 사랑하여라",
   "교육은 노년기를 위한 가장 훌륭한 대책이다.","세상에서 가장 아름다운 것은 물론 세상 그 자체이다.",
   "모든 운명은 그것을 인내함으로써 극복해야 한다.","하루라도 책을 읽지 않으면 입 안에 가시가 돋친다.",
   "행동하는 사람처럼 생각하고, 생각하는 사람처럼 행동하라.","용기는 대단히 중요하다. 근육과 같이 사용함으로써 강해진다.",
   "자기에게 덕이 없는 자는 타인의 덕을 시기한다.","잘못은 그것을 통하여 우리가 발전할 수 있는 훈련이다.","책이란 넓고 넓은 시간의 바다를 지나가는 배다.",
   "뭉치면 살고, 흩어지면 죽는다.","몇 마디 말에 많은 뜻을 담고, 말은 간단히 하라","부러지는 것보다 굽는 것이 낫다.","좋은 울타리는 선한 이웃을 만든다."
   
   
   ]
ja=["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"]
mo=["ㄱ","ㄴ",'ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㄲ','ㄸ','ㅃ','ㅆ','ㅉ']
eng=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
     "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n=1
m=1
o=0


print("몇문제를 풀지 입력하시오")
b=int(input())
print("준비되면 1 또는 2 또는 3 또는 4 또는 5를 눌러 주세요.\n(1=한글 2=영어 3=한글모음연습 4=한글자음연습 5=알파벳 연습)")
a=int(input())
while a!= 1 or a!= 2 or a!=3 or a!=4 or a!=5:
    if  a== 1 or a== 2 or a==3 or a==4 or a==5:
        break

    print("올바른 값을 입력해주세요.")
    a=int(input())
cntt=0
cnt=0
cnttt=0
start=time.time()

if a==2:
    q=random.choice(w)
    while n <= b:
        print("\n*문제",n)
        print(q)
        x=input()
        if q==x:
            print('통과!')
            n=n+1
            q=random.choice(w)
            cnt=cnt+1
            cntt=cntt+len(x)
        else:
            print("오타!")
            n=n+1
            q=random.choice(w)
            cntt=cntt+len(x)
            cnttt=cnttt+1
if a==3:
    q=random.choice(ja)
    while n <= b:
        print("\n*문제",n)
        print(q)
        x=input()
        if q==x:
            print('통과!')
            n=n+1
            q=random.choice(ja)
            cnt=cnt+1
            cntt=cntt+len(x)
        else:
            print("오타!")
            n=n+1
            q=random.choice(ja)
            cntt=cntt+len(x)
            cnttt=cnttt+1

if a==4:
    q=random.choice(mo)
    while n <= b:
        print("\n*문제",n)
        print(q)
        x=input()
        if q==x:
            print('통과!')
            n=n+1
            q=random.choice(mo)
            cnt=cnt+1
            cntt=cntt+len(x)
        else:
            print("오타!")
            n=n+1
            q=random.choice(mo)
            cntt=cntt+len(x)
            cnttt=cnttt+1

elif a==5:
    r=random.choice(eng)
    while m <= b:
        print("\n*문제",m)
        print(r)
        y=input()
        if r==y:
            print('통과!')
            m=m+1
            r=random.choice(eng)
            cnt=cnt+1
            cntt=cntt+len(y)
        else:
            print("오타!")
            m=m+1
            r=random.choice(eng)
            cntt=cntt+len(y)
            cnttt=cnttt+1
            
elif a==1:
    r=random.choice(v)
    while m <= b:
        print("\n*문제",m)
        print(r)
        y=input()
        if r==y:
            print('통과!')
            m=m+1
            r=random.choice(v)
            cnt=cnt+1
            cntt=cntt+len(y)
        else:
            print("오타!")
            m=m+1
            r=random.choice(v)
            cntt=cntt+len(y)
            cnttt=cnttt+1

fo=open("점수파일.txt",'a')

end = time.time()                 
et = end - start
ave=cntt/et*60
ave=format(ave, ".2f")
et = format(et, ".2f")

point=float(ave)*float(cnt)
point=format(point,".2f")
li[9]=float(point)
print("\n평균 타수 :",ave)
print("타자 시간 :", et, "초")
print("맞춘 개수 :",cnt)
print("틀린 개수 :",cnttt)
li.sort(reverse=True)
print("점수 : ",point,"\n")


fo.writelines([point])
fo.write('\n')
fo.close()

fo = open("점수파일.txt","r")
ship=int(len(fo.readlines()))
fo.seek(0)
so=fo.readlines()
for i in range(0,ship-1):

    yes=so[i]
    
    if li[9]<float(yes):
        li[9]=float(yes)
    li.sort(reverse=True)
    
fo.close()

for i,j  in enumerate(li):
     print(i+1,"등", j,'점')

os.system("pause")
    

