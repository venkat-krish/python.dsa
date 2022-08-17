

class LinearSort:

    def bubble_sort(self, vList):
        '''
        Linear sorting algorithm and non-efficient one takes O(n2)
        :param vList:
        :return:
        '''

        for i in range(0, len(vList)):
            for j in range(0, len(vList)):
                if vList[i] < vList[j]:
                  vList[i], vList[j] = vList[j], vList[i]
        return vList


