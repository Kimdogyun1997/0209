# 깊이 우선 탐색은 스택을 사용.

# < 재귀 함수>




#피보나치 함수

# def fibo(n) :
# 	if n == 0 :
# 		return 0
# 	elif n == 1 :
# 		return 1
# 	else :
# 		return fibo(n-1) + fibo(n-2)
#
# print('피보나치 수 --> 0 1 ', end='')
# for i in range(2, 20) :
# 	print(fibo(i), end=' ')
#
#
#

# 회문

## 함수 선언 부분 ##
def palindrome(pStr) :
	if len(pStr) <= 1 :
		return True

	if pStr[0] != pStr[-1] :
		return False

	return palindrome(pStr[1:len(pStr)-1])


## 전역 변수 선언 부분 ##
strAry = ["reaver", "kayak", "Borrow or rob", "주유소의 소유주", "야 너 이번주 주번이 너야", "살금 살금"]

## 메인 코드 부분 ##
for testStr in strAry :
	print(testStr, end = '--> ' )
	testStr = testStr.lower().replace(' ','')
	if palindrome(testStr) :
		print('O')
	else :
		print('X')






import tkinter as tk

memons = [None for _ in range(100)]
memons[0], memons[1] = 0, 1


def fact_recu(n):
	if n == 1:
		return 1
	else:
		return n * fact_recu(n-1)


def factorial_input():
	lbl_result.config(text=f"계산기 출력 결과: {fact_recu(int(en_num_input.get()))}")
	input_number = (int(en_num_input.get()))


def fibonacci_input():
	lbl_result.config(text=f"계산기 출력 결과: {fibo_memo_recu(int(en_num_input.get()))}")

win = tk.Tk()  # 윈도우 생성
win.title("Calculator")  # 피보나치, 팩토리얼 계싼기
win.geometry("250x150")
print(fact_recu(5))

en_num_input = tk.Entry()  # 텍스트 입력상자
lbl_result = tk.Label(text = "계산기 출력:")
btn_fact = tk.Button(text = "팩토리얼", command=factorial_input)
btn_fibo = tk.Button(text = "피보나치", command= factorial_input)

en_num_input.pack()
lbl_result.pack()
btn_fact.pack(fill='x')
btn_fibo.pack(fill='x')

win.mainloop()



import random as r


# 함수 선언 부분 ##
def findMinIdx(ary):
	minIdx = 0
	for i in range(1, len(ary)):
		if (ary[minIdx] < ary[i]):  # 내림차순
			minIdx = i
	return minIdx


# 전역 변수 선언 부분 ##
before = [r.randint(0,200) for _ in range(10)]  #
print(before)
after = []

# 메인 코드 부분 ##
print('정렬 전 -->', before)
for _ in range(len(before)):
	minPos = findMinIdx(before)
	after.append(before[minPos])
	del (before[minPos])
print('정렬 후 -->', after)



## 함수 선언 부분 ##
def quickSort(ary):
	n = len(ary)
	if n <= 1:  # 정렬할 리스트의 개수가 1개 이하면
		return ary

	pivot = ary[n // 2]  # 기준값을 중간값으로 지정
	leftAry, rightAry = [], []

	for num in ary:
		if num < pivot:
			leftAry.append(num)
		elif num > pivot:
			rightAry.append(num)

	return quickSort(leftAry) + [pivot] + quickSort(rightAry)


## 전역 변수 선언 부분 ##
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)


import random as r

## 함수 선언 부분 ##
def quickSort(ary):
	n = len(ary)
	if n <= 1:  # 정렬할 리스트의 개수가 1개 이하면
		return ary

	pivot = ary[n // 2]  # 기준값을 중간값으로 지정
	leftAry, rightAry = [], []

	for num in ary:

		if num > pivot:
			leftAry.append(num)

		elif num < pivot:
			rightAry.append(num)


	return quickSort(leftAry) + [pivot] + quickSort(rightAry)


## 전역 변수 선언 부분 ##
dataAry = [r.randint(0,200) for _ in range(20)]
print(dataAry)

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)



