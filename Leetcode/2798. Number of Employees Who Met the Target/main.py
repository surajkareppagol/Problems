def numberOfEmployeesWhoMetTarget(hours: list, target: int) -> int:
    print(len([i for i in hours if i >= target]))


numberOfEmployeesWhoMetTarget([1, 2, 3, 0, 0, 1], 2)
