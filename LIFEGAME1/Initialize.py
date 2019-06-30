
import random

def big_bang(stage):
    """
    初期化(生命の誕生)
    """
    #:HACK
    for y_i in range(stage.YMax):
        for x_j in range(stage.XMax):
            stage[y_i][x_j] = random.randint(0,1)
    return stage
