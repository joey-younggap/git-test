def get_even(num):
    try:
        if num % 2 == 0:
            return "짝수 입니다."
        else:
            return "홀수 입니다."
    except TypeError:
        return "숫자를 입력해 주세요."
