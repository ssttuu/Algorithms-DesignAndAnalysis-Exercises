


def count( array, length):
	if length == 0:
		return 0

	x = count( array[:length/2] )
	y = count( array[length/2:] )
	z = countSplitInv( 
