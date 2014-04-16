def rotate_search(target, array):
    # return -1 if none found

    def _issorted(low, high, pivot, array):
        print "\tissorted: ", low, high
        if low == high:
            return True
        elif (high - low + 1) == 2:
            return array[low] < array[high]
        else:
            return array[low] < array[pivot] and array[pivot] < array[high]

    def _finder(low, high, array, target):
        pivot = low + (high-low)/2
        print "low:", low, "high:", high, "pivot:", pivot
        # CONSTRAINT, one item arrays will match here
        if pivot == low and low == high:
            if target != array[pivot]:
                return -1

        if target == array[pivot]:
            return pivot

        if _issorted(low, high, pivot, array):
            if target > array[pivot]:
                return _finder(pivot+1, high, array, target)
            else:
                return _finder(low, pivot-1, array, target)
        else:
            lowpivot = low + (pivot-low)/2  
            hipivot  = (pivot+1) + (high-(pivot+1))/2  
            print 'lowpivot:', lowpivot, 'hipivot', hipivot
            if  (_issorted(low, pivot, lowpivot, array) and 
                 _issorted(pivot+1, high, hipivot, array)):
                print '----- 1'
                #import pdb; pdb.set_trace()
                # WE KNOW: target != array[pivot]
                if target >= array[low] and target < array[pivot]:
                    return _finder(low, pivot-1, array, target)
                else:
                    return _finder(pivot+1, high, array, target)

            elif (not _issorted(low, pivot, lowpivot, array) and 
                      _issorted(pivot+1, high, hipivot, array)):
                print '----- 2'
                if target < array[pivot+1] or target > array[high]:
                    return _finder(low, pivot-1, array, target)
                else: 
                    return _finder(pivot+1, high, array, target)

            elif (not _issorted(pivot+1, high, hipivot, array) and
                      _issorted(low, pivot, lowpivot, array)):
                print '----- 3'
                if target > array[pivot] or target < array[low]:
                    return _finder(pivot+1, high, array, target)
                else:
                    return _finder(low, pivot-1, array, target)

            else:
                print '----- 4'
                return -1

    return _finder(0, len(array)-1, array, target)
