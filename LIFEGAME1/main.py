#!/usr/bin/env python3

from pprint import pprint

 
from StageVisalize import visalize
from Initialize import big_bang
import LifeGameRules
from Stage import Stage



def redraw(stage):
    """
    ステージを書き直す
    """
    #:HACK
    new_stage = Stage()

    for y_i in range(1, stage.YMax-1):
        for x_j in range(1, stage.XMax-1):

            #生命が存在しないとき
            if stage[y_i][x_j] == 0:
                new_stage[y_i][x_j] = LifeGameRules.rule_1(stage, x_j, y_i)

            #生命が存在するとき
            elif stage[y_i][x_j] == 1:
                new_stage[y_i][x_j] = LifeGameRules.rule_2(stage, x_j, y_i)
            
    return new_stage


def main():
    #ステージの設立
    generation_stage = Stage()
    #初期化
    generation_stage = big_bang(generation_stage)

    #ゲームスタート
    while True:
        try:
            #可視化
            visalize(generation_stage)
            #ライフゲームのルールに則り、変化
            generation_stage = redraw(generation_stage)
            #コマ送り
            key = input()

            #ctrl + C で終了
        except KeyboardInterrupt:
            print('end of game')
            break

if __name__ == "__main__":
    main()
