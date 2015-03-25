"""
Change Problem

Find the minimum number of coins needed to make change.

Given: An integer money and an array Coins of positive integers.

Return: The minimum number of coins with denominations Coins that changes money.
---------------
Algorithm = ***

"""



'''Functions'''

def MoneyChanger (money, coinArray):
	''' Returns the minimum number of coins with denominations Coins that changes money. Dynamic Programming Approach.'''

	#The array that contains the minimum number of coins needed for a particular amount
	minCoinsList = [0]+[(money/min(coinArray))+1]*money

	for i in xrange(1, money + 1):
		for coin in coinArray:
			if i >= coin:
				if minCoinsList[i - coin] < minCoinsList[i]:
					minCoinsList[i] = minCoinsList[i-coin] + 1
	return minCoinsList[money]


'''Input/Output'''

with open('Data/rosalind_5a.txt') as inputData:
	money = int(inputData.readline().strip())
	coinArray = map(int, inputData.readline().strip().split(','))


answer = str(MoneyChanger(money,coinArray))

print answer

with open('Ros5A_Answer', 'w') as outputData:
	outputData.write(answer)




