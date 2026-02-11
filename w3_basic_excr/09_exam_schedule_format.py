# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014


def exam_time_writer(time: tuple[int]) -> str:
    if 0<= time[1] > 12:
        return f"Months can't exceed 12 or less than 1"
    if 0<= time[0] > 31:
        return f"date can't exceed 31 or less than 0"
    formated_text = (
        f"The examination will start from : {time[0]} / {time[1]} / {time[2]}"
    )
    return formated_text


exam_st_date = (11, 12, 2014)
res = exam_time_writer(time=exam_st_date)
print(res)
