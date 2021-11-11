# back tracking
# state space tree
# prunning
# DFS

# promising

# abs : 절대값
# 대각선은 두 값의 차의 절대값이 같은지 확인
def is_available(candidate, current_col):
    # 현재까지 확인된 퀸의 위치가 담겨있는 candidate 리스트와 현재 확인 중인 column 값을 가져와서 가능한지 확인하는 함수
    current_row = len(candidate)
    # row는 당연 한 칸씩 내려오다 보니, 현재까지 누적된 각 row 별 퀸의 위치의 갯수가 바로 현재 row의 값이 된다.
    # 한 행에 하나씩 집어넣어 놨기 때문에, candidate에 len을 통해 현재 행을 구할 수 있다.
    for queen_row in range(current_row):
        # 지금까지 누적된 값들을 하나씩 넣어서 현재 column 값과 위치 비교를 실시한다.
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            if candidate[queen_row] == current_col:
                print(str(current_col)+'는 직선에 위치합니다.')
            else:
                print(str(current_col)+'는 대각선에 위치합니다.')
            # 좌측 조건은 직선 / 우측 조건은 대각
            return False
        # 조건에 해당되지 않는다면 True를 리턴한다.
    return True



def dfs(N, current_row, current_candidate, final_result):
    if current_row == N:
        # 마지막 row라면 final_result로 넣는다.
        print(current_candidate[:])
        final_result.append(current_candidate[:]) # [:] 얇은 복사? pop을 해도 영향도가 없다.
        return
    for candidate_col in range(N): # 사각형의 길이만큼 column값을 대입하며 가능한 값인지 판단한다.
        if is_available(current_candidate, candidate_col):
            print('candidate_col: ' + str(candidate_col))
            current_candidate.append(candidate_col) # is_available 함수를 통과한 column 값은 current_candidate에 넣는다.
            dfs(N, current_row+1, current_candidate, final_result) # 재귀함수로 한 칸 더 늘려서 현재까지 candidate를 확인한다.
            # 가장 최근 요소 제거 - 백트래킹
            # dfs를 재귀로 호출하면서 한 번에 끝까지 못가고(return 까지 못가고) 여기로 온다면 pop 해야지,,, 실패한거니까!!!!!!!!!!!!!
            print(current_candidate)
            current_candidate.pop()
            print(current_candidate)

def nQueen(N):
    final_result = []
    dfs(N, 0, [], final_result)
    return final_result

print(nQueen(4))




