# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"
def compWith100( num ):
    # if not isinstance(num, int):
    #     print num, "is not an integer"
    if num >= 100:
        print num, "- That's a big number!"
    else:
        print num, "- That's a small number"

num = input( "Integer please ... " )
compWith100( num )

# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."
def compStringLengthWith50( strr ):
    if len( strr ) >= 50:
        print strr, "- Long sentence."
    else: print strr, "- Short sentence."

strr = raw_input("Sentence please ... ")
compStringLengthWith50( strr )

# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]

def compListLengthWith10( checkedList ):
    listLength = len( checkedList )
    if listLength >= 10:
        print checkedList, "- Big list!"
    else: print checkedList, "- Short list."

compListLengthWith10( aL )
compListLengthWith10( mL )
compListLengthWith10( lL )