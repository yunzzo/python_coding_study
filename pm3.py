num = int(input().strip())
if num == 1:
    for i in range(65, 91):
        print(chr(i), end="")

else:
    for i in range(97, 123):
        print(chr(i), end="")
# import string

# string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
# string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits # 숫자 0123456789


# list.sort() 원본에 변형을 준다
# list1 = sorted(list) 원본에 변형없이 새로운 리스트
