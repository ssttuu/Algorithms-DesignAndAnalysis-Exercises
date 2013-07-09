import os
import sys


def mergeSort( array):
	arrayLength = len(array)
	if arrayLength == 1:
		return array

	lSort = mergeSort( array[:arrayLength/2] )
	rSort = mergeSort( array[arrayLength/2:] )

	li=ri=ai=0

	while li < len( lSort):
		if ri < len( rSort):
			if lSort[li] <= rSort[ri]:
				array[ai] = lSort[li]
				li += 1
			else:
				array[ai] = rSort[ri]
				ri += 1
		else:
			array[ai] = lSort[li]
			li += 1
		ai += 1

	while ri < len( rSort):
		array[ai] = rSort[ri]
		ri += 1
		ai += 1

	return array


if __name__ == "__main__":
	f = open( sys.argv[1], 'r')
	toBeSorted = f.readlines()
	toBeSorted = [int(l.strip()) for l in toBeSorted if l != ""]
	print mergeSort( toBeSorted)

