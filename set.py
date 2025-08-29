
#Set is a collection of unordered , unique , finite elements. 
# Mutable, 
# can't indexing because this is unordered.
#set is mutable but set elements are immutable.
# set1={1,1.1,'string',[1,1,2],'string'}
# TypeError: unhashable type: 'list'
# print(set1)


#forzenset

# frozenset is immutable

frzs1 = frozenset([1,2,3,1,'str1','str2'])
print(frzs1)

#None

vebl1 = None
print(type(vebl1))