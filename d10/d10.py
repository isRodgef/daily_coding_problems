from time import sleep


def shed(func, n):
	sleep(n/1000)
	func(n)

