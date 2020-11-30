    def longestMountain(self, A):
        N = len(A)
        ans = base = 0

        #while the base is less that len(A)-1 (< is the -1)
        while base < N:
            #set the end to the start of the left-boundary
            end = base
            if end + 1 < N and A[end] < A[end + 1]: #if base is a left-boundary
                #set end to the peak of this potential mountain
                while end+1 < N and A[end] < A[end+1]:
                    end += 1

                if end + 1 < N and A[end] > A[end + 1]: #if end is really a peak..
                    #set 'end' to right-boundary of mountain
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                    #record candidate answer
                    ans = max(ans, end - base + 1)
            #logic to move to next index
            base = max(end, base + 1)

        return ans
