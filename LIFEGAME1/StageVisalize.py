


def visalize(stage):
    for row in stage():
        for cell in row:
            if cell == 0:
                print("□",end="")
            else:
                print("■",end= "")
        print()

