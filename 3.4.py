number = int(input('정수를 입력하세요 : '))
print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?',
      number % 2 == 0 and 0 <= number <= 100)