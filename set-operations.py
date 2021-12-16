
## Add
## Add an new element to the set.
set1 ={'Mick', 'Brian', 'Jenny'}
set1.add('Adam')
print(set1)

## clear
## Remove all elements from the set.
set2 = {'Mick', 'Brian', 'Jenny'}
set2.clear()
print("Clear: ",set2)

## copy
## Return a shallow copy of the set.
set3 = {'Mick', 'Brian', 'Jenny'}
set4 = set3.copy()
print("Copy: ",set4)

## difference
## Return a new set with elements in the set and not in the other.
set5 = {'Mick', 'Brian', 'Jenny'}
set6 = {'Mick', 'Jenny'}
set7 = set5.difference(set6)
print("Difference: ",set7)



## intersection
## Return a new set with elements common to the set and another.
set11 = {'Mick', 'Brian', 'Jenny'}
set12 = {'Mick', 'Jenny'}
set13 = set11.intersection(set12)
print("Intersection: ",set13)

## intersection_update
## Update the set, keeping only elements found in it and another.
set14 = {'Mick', 'Brian', 'Jenny'}
set15 = {'Mick', 'Jenny'}
set14.intersection_update(set15)
print("Intersection_update: ",set14)

## isdisjoint
## Return True if two sets have a null intersection.
set16 = {'Mick', 'Brian', 'Jenny'}
set17 = {'Mick', 'Jenny'}
set18 = set16.isdisjoint(set17)
print("Isdisjoint: ",set18)

## issubset
## Report whether another set contains this set.
set19 = {'Mick', 'Brian', 'Jenny'}
set20 = {'Mick', 'Jenny'}
set21 = set19.issubset(set20)
print("Issubset: ",set21)

## issuperset
## Report whether this set contains another set.
set22 = {'Mick', 'Brian', 'Jenny'}
set23 = {'Mick', 'Jenny'}
set24 = set22.issuperset(set23)
print("Issuperset: ",set24)

## pop
## Remove and return an arbitrary set element.
set25 = {'Mick', 'Brian', 'Jenny'}
set25.pop()
print("Pop: ",set25)

## remove
## Remove an element from a set; it must be a member.
set26 = {'Mick', 'Brian', 'Jenny'}
set26.remove('Mick')
print("Remove: ",set26)

## symmetric_difference
## Return a new set with elements in either the set or other but not both.
set27 = {'Mick', 'Brian', 'Jenny'}
set28 = {'Mick', 'Jenny'}
set29 = set27.symmetric_difference(set28)
print("Symmetric_difference: ",set29)



## union
## Return a new set with elements from the set and all others.
set32 = {'Mick', 'Brian', 'Jenny'}
set33 = {'Mick', 'Jenny'}
set34 = set32.union(set33)
print("Union: ",set34)

## update
## Update the set with the union of itself and others.
set35 = {'Mick', 'Brian', 'Jenny'}
set36 = {'Mick', 'Jenny'}
set35.update(set36)
print("Update: ",set35)








