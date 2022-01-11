class Solution(object):
    def partitionLabels(self,S:str):
        '''
        :type S: str
        :rtype: List[int]
        '''
        last_index = {s: i for i, s in enumerate(S)}
        
        result =[]
        
        base_index =0
        
        final_index = 0
        
        for i, s in enumerate(S):
            base_index = max(base_index,last_index[s])
            
            if i ==  base_index:
                result.append(base_index - final_index +1)
                final_index = base_index +1
                
        return result

        