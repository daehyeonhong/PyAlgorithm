import math


def solution(users, emoticons):
    answer = []
    memberShipPlus = 0
    minimumRate = 40

    for user in users:
        minimumRate = min(user[0], minimumRate)
    
    new_var = minimumRate%10
    if new_var!=0:
        minimumRate-=new_var
        minimumRate += 10



    users = [[40, 10000], [25, 10000]]
    users = [[40, 10000], [30, 10000]]
    users = 3,4
    

    return answer




print(
    f'{solution([[40, 10000], [25, 10000]],[7000, 9000])}, result: {[1, 5400]}')
print(f'{solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],[1300, 1500, 1600, 4900])}, result: {[4, 13860]}')




'''
사용자	구매한 이모티콘	이모티콘 구매 비용	이모티콘 플러스 서비스 가입 여부
1	      2	       5   ,400	X
2	1, 2	10,300	O


users	                     emoticons	     result
[[40, 10000], [25, 10000]]	[7000, 9000]	[1, 5400]
[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]	[1300, 1500, 1600, 4900]	[4, 13860]
'''
