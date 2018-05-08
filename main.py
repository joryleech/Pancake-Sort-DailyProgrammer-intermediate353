
def flip(fliplist,endIndex):
	if endIndex >len(fliplist)-1:
		print("Improper List Indexes in flip")		
	sublist=[]
	for i in reversed(range(0,endIndex+1)):
		sublist.append(fliplist[i])
	for i in range(endIndex+1,len(fliplist)):
		sublist.append(fliplist[i])
	return sublist
def pancakeSort(fliplist):
	returnList=[fliplist]
	for i in range(0,len(fliplist)):
		currentListPos=len(fliplist)-i;
		largestNumPos=0;
		for y in range(1,currentListPos):
			if(fliplist[y]>fliplist[largestNumPos]):
				largestNumPos=y

		fliplist=flip(fliplist,largestNumPos)
		fliplist=flip(fliplist,currentListPos-1)
		returnList.append(fliplist)
	return returnList
def formatOutput(array):
	while(array[-1]==array[-2]):
		del array[-1]		
	output=str(len(array)-1)+" Flips: "
	for item in array:
		output+=(str(item))
		if not (item == array[-1]):
			output+=("->")
	
	print(output)
		
unformattedList=input("Please Input A List Of Numbers With Spaces Inbetween:\n")
fliplist=[]
for item in unformattedList.split():
	fliplist.append(int(item))
formatOutput(pancakeSort(fliplist))
