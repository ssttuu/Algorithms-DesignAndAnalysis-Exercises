#include <iostream>
#include <vector>
using namespace std;


void printArray( vector<int> * array ) {
	int l = (*array).size();
	for (int i=0; i < l; i++) {
		cout << (*array)[i] << ", ";
	}
	cout << endl;
}

vector<int> *  mergeSort( vector<int> * array, vector<int> * outArray, int * splitInv ) {
	int arrayLength = (*array).size();
	int lSize = arrayLength/2;

	vector<int> lSort( lSize);
	vector<int> rSort( arrayLength - lSize);

	if ( arrayLength == 1 ) {
		return array;
	}

	
}



int main() {
	vector<int> array1;
	for (int i=5; i >= 0; i--) {
		array1.push_back(i);
	}
	printArray( &array1);

	//mergeSort( array1 );

	printArray( &array1);
	
	vector<int> a(2);
	vector<int> b;

	b.push_back(5);
	b.push_back(2);

	a = b;
	a[0] = 33;
	printArray( &a);
	printArray( &b);

}


