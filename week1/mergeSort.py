import os
import sys


def mergeSort( array, splitInv=0):
	arrayLength = len(array)
	if arrayLength == 1:
		return array, splitInv

	lSort,lInv = mergeSort( array[:arrayLength/2], splitInv=0 )
	rSort,rInv = mergeSort( array[arrayLength/2:], splitInv=0 )

	splitInv += lInv + rInv
	li=ri=ai=0

	while li < len( lSort):
		if ri < len( rSort):
			if lSort[li] <= rSort[ri]:
				array[ai] = lSort[li]
				li += 1
			else:
				array[ai] = rSort[ri]
				ri += 1
				splitInv += len( lSort) - li
		else:
			array[ai] = lSort[li]
			li += 1
		ai += 1

	while ri < len( rSort):
		array[ai] = rSort[ri]
		ri += 1
		ai += 1

	return array, splitInv


if __name__ == "__main__":
	f = open( sys.argv[1], 'r')
	toBeSorted = f.readlines()
	toBeSorted = [int(l.strip()) for l in toBeSorted if l != ""]
	print mergeSort( toBeSorted)
	#print mergeSort( [1,2,4,3,5,6])
	#print mergeSort( [1,3,5,2,4,6])
