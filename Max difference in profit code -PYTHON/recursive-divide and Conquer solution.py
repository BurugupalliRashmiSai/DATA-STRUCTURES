def readData(filename):
    file=open(filename)
    return file

def getData(file):
    values={}
    for i in file.readlines()[0].split('\r'): 
        if "/" in i:
            data=map(int,i.split("/"))
            values[data[0]]=data[1]
    return values

def maxProfit_dc(values):
    print(values)
    arr=values.values()
    diff=[]
    for i in range (0,len(arr)-1): 
        diff.append(arr[i+1] - arr[i])
    print(diff)
    start, end, maximum=find_max_subarray(diff, 0, len(diff))
    return start+1, end+1, maximum
    
    
def writeOutput(lindex,hindex,maximum):
    f=open('Output.txt','w+')
    f.write("Maximum Profit (Divide and Conquer): {} \n".format(maximum))
    f.write("Day to buy: {} \n".format(lindex))
    f.write("Day to sell: {}".format(hindex))
    f.close()   
    
def find_max_subarray(diff, start, end):
    if start == end - 1:
        return start, end, diff[start]
    else:
        mid = (start + end)//2
        left_start, left_end, left_max = find_max_subarray(diff, start, mid)
        right_start, right_end, right_max = find_max_subarray(diff, mid, end)
        cross_start, cross_end, cross_max = find_max_crossing_subarray(diff, start, mid, end)
        if (left_max > right_max and left_max > cross_max):
            return left_start, left_end, left_max
        elif (right_max > left_max and right_max > cross_max):
            return right_start, right_end, right_max
        else:
            return cross_start, cross_end, cross_max

def find_max_crossing_subarray(diff, start, mid, end):
    sum_left = float('-inf')
    sum_temp = 0
    cross_start = mid
    for i in range(mid - 1, start - 1, -1):
        sum_temp = sum_temp + diff[i]
        if sum_temp > sum_left:
            sum_left = sum_temp
            cross_start = i
    sum_right = float('-inf')
    sum_temp = 0
    cross_end = mid + 1
    for i in range(mid, end):
        sum_temp = sum_temp + diff[i]
        if sum_temp > sum_right:
            sum_right = sum_temp
            cross_end = i + 1
    return cross_start, cross_end, sum_left + sum_right


file=readData('input.txt')
values=getData(file)
lindx,hindx,maximum=maxProfit_dc(values)
writeOutput(lindx,hindx,maximum)