W, H = map(int, input().split())
X, Y = map(int, input().split())
state = 0
opportunity = int(input())


def bottom2up(x, y):
    return x+1, y+1


def right2up(x, y):
    return x-1, y+1


def top2down(x, y):
    return x-1, y-1


def left2up(x, y):
    return x+1, y+1


print(f"W: {W}, H: {H} // X: {X}, Y: {Y}")
print(f"opportunity: {opportunity}")
print("===================")

while opportunity > 0:
    if (state == 1 and (1 <= X <= W-1 and 1 <= Y <= H-1)) or (X == W and (0 <= Y <= H)):
        state = 1
        X, Y = right2up(X, Y)
        print("right2up", X, Y)
    elif (state == 2 and (1 <= X <= W-1 and 1 <= Y <= H-1)) or ((0 <= X <= W) and Y == H):
        state = 2
        X, Y = top2down(X, Y)
        print("top2down", X, Y)
    elif (state == 3 and (1 <= X <= W-1 and 1 <= Y <= H-1)) or (X == 0 and 0 <= Y <= H):
        state = 3
        X, Y = left2up(X, Y)
        print("left2up", X, Y)
    else:
        state = 0
        X, Y = bottom2up(X, Y)
        print("bottom2up", X, Y)

    opportunity -= 1
    # print(opportunity)

print(X, Y)
