def solution(numbers, hand):
    answer = ''
    # 각 숫자의 좌표
    points = [
        (0, -2), 
        (-1, 1), (0, 1), (1, 1),
        (-1, 0), (0, 0), (1, 0),
        (-1, -1), (0, -1), (1, -1)
    ]
    # 현재 왼손 오른손의 좌표
    lp = (-1, -2)   # 왼손
    rp = (1, -2)    # 오른손
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            lp = points[n]
        elif n in [3, 6, 9]:
            answer += 'R' 
            rp = points[n]
        else:   # 가운데 키패드를 누르는 경우
            # 각 손과 키패드의 거리를 구함
            ld = abs(points[n][0] - lp[0]) + abs(points[n][1] - lp[1])
            rd = abs(points[n][0] - rp[0]) + abs(points[n][1] - rp[1])
            if ld == rd:    # 거리가 같은경우
                if hand == 'left':
                    answer += 'L'
                    lp = points[n]
                else:
                    answer += 'R'
                    rp = points[n]
            elif ld > rd:   # 오른손이 가까운 경우
                answer += 'R'
                rp = points[n]
            else:
    return answer
