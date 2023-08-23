# list - done

# tupple
# tupple is same as list but it is immutable

marks = (32,45,76,86,86)

print(marks.count(86))
print(marks.index(86))

# next data structure - set
# give only unique value and there is no concept of index in set, its unordered
marks = {32,45,76,86,86}
for score in marks:
    print(score)


# dictionary
# stores value in key pair
marks= {"english":78, "chemistry":57}
pirnt(marks["chemistry"])
marks["physics"] = 97 #add physics in dictionary data structure
print(marks)

marks["english"] = 76 # change the marks of english in dictionary
print(marks)

