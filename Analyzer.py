def data_analyzer(values):
    sumvalue=sum(values)
    minvalue=min(values)
    maxvalue=max(values)
    average=sum(values)/len(values)
    sort=sorted(values)
    above_avg=0
    for i in values:
        if(i<average):
            above_avg+=1
    return {
        "sum":sumvalue,
        "min":minvalue,
        "max":maxvalue,
        "avg":average,
        "above_avg":above_avg,
        "sort":sort
        }
values=[80,90,70,60,50]
print(data_analyzer(values))
