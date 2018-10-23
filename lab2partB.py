# CS 2302- Data Structures
# TR 10:20am-11:50am
# Instructor: Diego Aguirre
# Lab 2 Option B
# Submitted By: Noemi Hernandez
# Date last edited: 23 October 2018
# The purpose of this program is to read from a file a list
# user names and passwords, and check the list to see how many
# times a certain password was use, then print out the top
# 20 most used passwords from that list

class Node(object):
    password = ""
    count = -1
    next = None
###################################
    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next
###################################
    def insertNode(self, password, count):
        head= self
        #Sets the node to be the head if there is no head
        if head.count is -1:
            head.password= password
            head.count= count
        #goes through the linked list until it reaches the end of the linked list
        while head.next is not None:
            head= head.next
        #once it reaches the end of the linked list it inserts the new node to the linked list
        head.next= Node(password, count, None)
###################################
    def length(self):
        head= self
        i=0
        #returns 0 is there is nothing in the linked list
        if head == None:
            return 0
        #Goes through the linked list adding one each time the condition holds true
        while head is not None:
            i+=1
            head= head.next
        #returns the length of the linked list
        return i
############End of Node Class############
###################################
def createLinkedList(filename):
    node= None
    line=""
    myList=None
    #opens the file 
    try:
        f= open(filename)
        #runs as long as the file has a line to read
        for line in f:
            #breaks up the line read so that you can get the passwords not the usernames
            temp= line.rsplit()
            try:
                #gets only the password from the file and creates a node
                node= Node(temp[1], 1, None)
            except IndexError:
                #if the line did not have a password it sets the password to an empty String and then creates the node
                node= Node("", 1, None)
            #if the list is empty the first node created is not the head of the linked list
            if myList== None:
                myList= node 
            #if there already is a head it stores it as a current value
            else:
                curr= myList
                #traverses through the linked list
                while curr is not None:
                    #if the given nodes password value already exsits it adds one to the count and the current node
                    if node.password == curr.password:
                        curr.count+=1
                        node.count+=1
                    curr= curr.next
                #if the current nodes password has not already been added to the linked list it will now be added
                if node.count == 1:
                    myList.insertNode(node.password, node.count)
    except FileNotFoundError:
        print(filename, "was not found, or does not exsit.")

    return myList
###################################
def createDict(fileName):
    dic = {}
    temp=[]
    listWithDuplicates=[]
    line=""
    #opens the given file
    try:
        f= open(fileName)
        #runs so long as the file has a line to read
        for line in f:
            #splits the line up so that you can only get the passwords
            temp= line.rsplit()
            try:
                #gets only the password from the file and adds it to a list object
                listWithDuplicates.insert(0, temp[1])
            except IndexError:
                #if there was no password it gets set to and empty string then added to a list object
                listWithDuplicates.insert(0, "")
    except FileNotFoundError:
        print(fileName, "was not found, or does not exsit.")
        
    #traverses to the list object    
    for item in listWithDuplicates:
        #if the item in the list exsits within the dictionary it adds 1 to key- value of the dictionary
        if item in dic: # You can assume this operation takes O(1)
            dic[item] = dic[item] + 1
        #if it does not exsits in the dictionary it adds the password as a ney key and sets its key- value to 1
        else:
            dic[item] = 1
       
    return dic
###################################
def createLLusingDic(dic):
    head= None
    myList= None
    temp= None
    #traverses through the dictionary
    for key in dic:
        #if the linked list does not exsits it adds the first item in the dictionary as the head node
        #node is created by giving the key as the password and the key- value as the count for the node
        if head == None:
            head= Node(key,dic[key], None)
            myList=head
        else:
            #inserts the node to the linked list so long as there is something new to add
            myList.insertNode(key, dic[key])
    
    return myList
###################################
def mergeSort(myList):
    #if the linked list is none returns the empty linked list
    if myList == None or myList.next == None:
        return myList
    length = myList.length()
    pivot = length//2
    temp = myList
    #runs half of the length of the linked list minus 1 so that temp starts halfway through the linked list
    for i in range(pivot - 1):
        temp = temp.next
    #creates a duplicate list that starts at the halfway point of the original linked list
    halfMyList = temp.next
    #breaks the list in half
    temp.next = None
    #recursively calls the fisrt half of the linked list until it can no longer be broken in two
    firstHalfOfList = mergeSort(myList) 
    #recursively calls the second half of the linked list until it can no longer be broken in two
    secondHalfOfList = mergeSort(halfMyList)
    #if the node in the first half is greater than the second half node
    if(firstHalfOfList.count > secondHalfOfList.count):
        #mergeList first node is set to be the first half's node
        mergedList = firstHalfOfList
        firstHalfOfList = firstHalfOfList.next
    else:
        #mergeList first node is set to be the second half's node
        mergedList = secondHalfOfList
        secondHalfOfList = secondHalfOfList.next
    #temp is now set to be the merged linked list
    temp = mergedList
    #runs so long as BOTH splitLists have something in them
    while firstHalfOfList is not None and secondHalfOfList is not None:
        #if the node in the first half is greater than the second half node
        if(firstHalfOfList.count > secondHalfOfList.count):
            #the next node in temp is set to be the node from the first half
            temp.next = firstHalfOfList
            #goes on to the next node in the first half but not the second half
            firstHalfOfList = firstHalfOfList.next
        else:
            #the next node in temp is set to be the node from the second half
            temp.next = secondHalfOfList
            #goes on to the next node in the second half but not the first half
            secondHalfOfList = secondHalfOfList.next
        #moves through or temp linked list so that we can keep adding to the end of it
        temp = temp.next
    #excecutes if the second half ran out of nodes and runs so long as the first half has nodes in it and adds the remaining nodes to temp
    while firstHalfOfList is not None:
        temp.next = firstHalfOfList
        firstHalfOfList = firstHalfOfList.next
        temp = temp.next 
    #excecutes if the first half ran out of nodes and runs so long as the second half has nodes in it and adds the remaining nodes to temp    
    while secondHalfOfList is not None:
        temp.next = secondHalfOfList
        secondHalfOfList = secondHalfOfList.next
        temp = temp.next 
    
    return mergedList
###################################
def bubbleSort(myList):
    curr = myList
    while curr is not None:
        pointer = curr.next
        while pointer is not None:
            #If the current count is less than pointer count, swap both the count values and password values
            if curr.count < pointer.count:
                curr.count, pointer.count = pointer.count, curr.count
                curr.password, pointer.password = pointer.password, curr.password

            pointer = pointer.next

        curr = curr.next
    return myList
###################################
def printTop20(myList):
    print("The top 20 most used passwords are:")
    for i in range(20):
        if myList is not None:
            print(myList.password, "it was used", myList.count, "time(s)")
            myList= myList.next
        elif myList is None:
            print("There were less than 20 Passwords, therefore there is no top 20 most used.")
            return
###################################
def main():  
    valid = True
    fileExsits= False
    
    while valid:
        if fileExsits== False:
            print("Type name of your file: (Include .txt, .dat, etc)")
            filename= input("(Include .txt, .dat, etc) ")
            print("What would you like to do?")
        
        print("1.) Create a linked list straight from the file.")
        print("2.) Create a linked list using a dictionary.")
        print("3.) Merge sort your linked list and print the top 20 most used passwords.")
        print("4.) Bubble sort your linked list and print the top 20 most used passwords.")
        print("5.) Exit the program.")
        
        try:
            function= int(input("Please type the number only: "))
            
            if function == 1:
                #Creates a linked list directly from the file
                myList= createLinkedList(filename)
                if myList is not None:
                    fileExsits= True
            elif function == 2:
                #Creates a Dictionary of the passwords
                dic= createDict(filename)
                #Creates a Linked List using the Dictionary
                myListFromDict= createLLusingDic(dic)
                if myListFromDict is not None:
                    fileExsits= True
            elif function == 3:
                myList= mergeSort(myList)
                myListFromDict= mergeSort(myListFromDict)
                if myList is not None:
                    printTop20(myList)
                    print("--------------------------")
                if myListFromDict is not None:
                    printTop20(myListFromDict)
                    print("--------------------------")

            elif function == 4:
                myList= bubbleSort(myList)
                myListFromDict= bubbleSort(myListFromDict)
                if myList is not None:
                    printTop20(myList)
                    print("--------------------------")
                if myListFromDict is not None:
                    printTop20(myListFromDict)
                    print("--------------------------")
            elif function== 5:
                print("Thank you, have a nice day :)")
                valid= False
            else:
                print("Number must be between 1- 5")
                
        except ValueError:
            print("Invalid input please try again.")
main()
