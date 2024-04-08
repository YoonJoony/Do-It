for i in range(1, 100000):
    L, P, V = map(int, input().split())

    if L+P+V == 0:
        break

    cam_div = V // P
    cam_mod = V % P
    if cam_mod > L:
        cam_mod = L
    print(f"Case {i}: {L * cam_div + cam_mod}")

# 5 8 20일 경우
# 5 + 3
# 5 + 3 ==> 여기까지 16일 씀
# 5 + 3 ===> 여기서부터 4일만 써야됨.
# 총 24일