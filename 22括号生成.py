r'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

1 <= n <= 8
'''

results = {0:[""],1:["()"]}

def rec(n):
    if n in results:
        return results[n]
    results[n] = []
    for i in range(0,n):
        first_components = rec(i)
        j = n-1-i
        second_components = rec(j)
        # print(n,i,j, first_components,second_components)

        for a in first_components:
            for b in second_components:
                results[n].append(f'({a}){b}')
    return results[n]

rec(8)
print(results)
        

