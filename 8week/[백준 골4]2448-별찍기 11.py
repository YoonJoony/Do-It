import sys

input = sys.stdin.readline


def paper_11(size):
    if size == 3:
        L = []
        L.append(" " * 2 + "*" + " " * 2)
        L.append(" " + "* *" + " ")
        L.append("*" * 5)
        return L

    Stars = paper_11(size // 2)
    L = []

    for S in Stars:
        L.append(" " * (size // 2) + S + " " * (size // 2))
    for S in Stars:
        L.append(S + " " + S)
    return L


n = int(input())
print("\n".join(paper_11(n)))
