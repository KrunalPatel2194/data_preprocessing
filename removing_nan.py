def remove_missing_values(data, strategy = 'mean', missing_value = 'nan'):
    columns = len(data[0])
    i = j  = 0
    indexes = []
    meanl = []
    while i < columns:
        indexes.append(i)
        mean = count = 0
        for index, item in enumerate(data[:,i]):
            if(np.isnan(item)  == False):
                count = count + 1
                mean = mean + item
        mean = mean/count 
        i = i + 1
        meanl.append(mean)
    while j < columns:
        for index, item in enumerate(data[:,j]):
            if(np.isnan(item)):
                data[index,j] = meanl[j]
        j = j +1
    return data
