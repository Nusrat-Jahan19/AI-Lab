def SumSeries(start,n,interval):
    if n == 1:
        return start
    return start + (n-1)*interval + SumSeries(start,n-1,interval)

print('the sum of 1st n terms of an equal interval series: ')

start = int(input('Enter the first element of the series: '))
n = int(input('Number of 1st n terms : '))
interval = int(input('Interval among terms of the series: '))
Total_Sum = SumSeries(start,n,interval)
print('The sum is: ',Total_Sum)
