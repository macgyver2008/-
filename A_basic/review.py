class HangulNum:
    def __init__(self, hangul_num="영"):
        self.hangul_num = hangul_num
    def __int__(self):
        num = ""
        for hnum in self.hangul_num:
            if hnum == "영":
                num += "0"
            elif hnum == "일":
                num += "1"
            elif hnum == "이":
                num += "2"
            elif hnum == "삼":
                num += "3"
            elif hnum == "사":
                num += "4"
            elif hnum == "오":
                num += "5"
            elif hnum == "육":
                num += "6"
            elif hnum == "칠":
                num += "7"
            elif hnum == "팔":
                num += "8"
            elif hnum == "구":
                num += "9"
            else:
                raise ValueError(self.hangul_num + "은 정수로 변환할  수 없습니다")

        return int(num)

Kr = HangulNum("일일영일영일영일영일영일영일영영영영영일일일영영일")
nm_num = int(Kr)
print(nm_num)




class HangulFlNum:
    def __init__(self, hangul_num="영"):
        self.hangul_num = hangul_num
    def __float__(self):
        num = ""
        for hnum in self.hangul_num:
            if hnum == "영":
                num += "0"
            elif hnum == "일":
                num += "1"
            elif hnum == "이":
                num += "2"
            elif hnum == "삼":
                num += "3"
            elif hnum == "사":
                num += "4"
            elif hnum == "오":
                num += "5"
            elif hnum == "육":
                num += "6"
            elif hnum == "칠":
                num += "7"
            elif hnum == "팔":
                num += "8"
            elif hnum == "구":
                num += "9"
            elif hnum == "점":
                num += "."
            else:
                raise ValueError(self.hangul_num + "은 소수로도 변환할  수 없습니다")

        return float(num)


Krfl = HangulFlNum("삼점일사일오구일")
nm_num = float(Krfl)
print(nm_num)

class IntegerToHangul:
    def __init__(self, int_num=0):
        self.int_num = int_num
    def __str__(self):
        h = ""
        for int_num in str(self.int_num):
            if int_num == "0":
                h += "영"
            elif int_num == "1":
                h += "일"
            elif int_num == "2":
                h += "이"
            elif int_num == "3":
                h += "삼"
            elif int_num == "4":
                h += "사"
            elif int_num == "5":
                h += "오"
            elif int_num == "6":
                h += "육"
            elif int_num == "7":
                h += "칠"
            elif int_num == "8":
                h += "팔"
            elif int_num == "9":
                h += "구"
            else:
                raise ValueError(self.int_num + "은 문자열로 변환할  수 없습니다")
        return str(h)

itkr = IntegerToHangul(113232343)
kr = str(itkr)
print(kr)


from datetime import datetime

class MyPlan:
    def __init__(self, d_day):
        self.d_day = d_day

    def __bool__(self):
        now = str(datetime.today()).split(" ")[0]
        return now == self.d_day



plan = MyPlan("2022-06-18")

print(plan)
