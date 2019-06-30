
def get_3_3_around(stage, x_center, y_center):
    """
    ３かける３を取り出す。
    """
    around_area = []
    for y_i in range(y_center-1, y_center+2):

        row = []
        for x_j in range(x_center-1, x_center+2):
            row.append(stage[y_i][x_j])
        
        around_area.append(row)
    
    return around_area


def key_count(area, key_num):
    #HACK:名前
    sum = 0
    for row in area:
        sum += row.count(key_num)
    return sum
