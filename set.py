# a=set()
# print(type(a))
# set1={1,6,4,'abc'}
# print(type(set1))

# days=(["Monday","Tuesday","Wednesday","Thursday"])
# print(days)
# print(type(days))
# for i in days:
#     print(i)

# months=set(["january","february","march","april","may","june"])
# print(months)
# months.add("july")
# print(months)

# months.update(["september","august"])
# print(months)

# months.discard("january")
# print(months)

# months.remove("september")
# print(months)



# print("set operations")
# days1={"monday","tuesday","wednesday","thursday"}
# days2={"friday","saturday","sunday"}
# print("union",days1|days2)

# days3={"monday","tuesday","sunday","friday"}
# print("intersection:",days1&days3)


day1={"monday","tuesday","wednesday","thursday"}
day2={"monday","tuesday"}
day3={"monday","tuesday","friday"}
print("superset and subset")
print(day1>day2)
print(day1<day2)
print(day2==day3)
