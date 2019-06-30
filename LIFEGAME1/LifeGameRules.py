import Around


def rule_1(stage, x_j, y_i):
    """
    生命のいないところは、
    周囲にちょうど３個の生命がある場合に新しく生命が誕生します。
    """
    around_area = Around.get_3_3_around(stage, x_j, y_i)
    life_count = Around.key_count(around_area,1)
    if (life_count == 3):
        return 1
    else:
        return 0
            

def rule_2(stage, x_j, y_i):
    """
    生命がいるところは、
    周囲に２個、または３個の生命がいる場合に、そのまま生命が残ります。 
    そうでない場合には死んでしまいます。
    """
    around_area = Around.get_3_3_around(stage, x_j, y_i)
    life_count = Around.key_count(around_area,1) 

    #周囲のマスだけを数えるために、中央の生命の分だけ一つ減らす。
    life_count = life_count -1
    
    if (life_count==3)or(life_count==2):
        return 1
    else:
        return 0


