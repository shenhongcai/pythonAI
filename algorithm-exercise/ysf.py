""" 约瑟夫算法
据说著名犹太历史学家 Josephus 有过以下的故事：
在罗马人占领桥塔帕特后，39个犹太人与 Josephus 及他的朋友躲到一个洞中，
39个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，41个人排成一个圆圈，
由第1个人开始报数，每报数到第3人该人就必须自杀，然后再由下一个重新报数，
直到所有人都自杀身亡为止。然而 Josephus 和他的朋友并不想自杀，
问他俩安排的哪两个位置可以逃过这场死亡游戏？
"""
import collections
def ysf(a, b):
    d = collections.deque(range(1, a+1)) # 将每个人依次编号，放入到队列中
    while d:
        d.rotate(-b) # 队列向左旋转b步
        print(d.pop()) # 将最右边的删除，即自杀的人

if __name__ == '__main__':
    ysf(41,3) # 输出的是自杀的顺序。最后两个是16和31，说明这两个位置可以保证他俩的安全。