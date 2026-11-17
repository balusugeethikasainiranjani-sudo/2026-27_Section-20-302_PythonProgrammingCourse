def total_and_average(subject_1,subject_2,subject_3):
    total=subject_1+subject_2+subject_3
    average = total/3
    return total,average

s1,s2,s3=21,31,4
total,average = total_and_average(s1,s2,s3)
print("total:",total)
print("average:",average)