def find_stu_name_with_stu_no(target_stu_no):
    stu_no = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]
    for i in range(len(stu_no)):
        if stu_no[i] == target_stu_no:
            return stu_name[i]
    return "?"


print(find_stu_name_with_stu_no(39))
print(find_stu_name_with_stu_no(14))
print(find_stu_name_with_stu_no(101))
