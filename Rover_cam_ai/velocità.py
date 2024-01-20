def speed(x1 : int, x2 : int) -> int:
    if abs(x1 - x2) >= 500 :
        velocità = 0.5
    else:
        velocità = ((abs(x1 - x2)) * 0.5) / 500
    return abs(velocità - 0.5)

