def numberOfEmployeesWhoMetTarget(hours: list, target: int) -> int:
    total = 0
    for i in hours:
        if i >= target:
            total += 1
    print(total)
