'''print This pattern
       *
      * *
     * * *
    * * * *   '''
row=4
for i in range(1,row+1) :
    print(" "*(row-i),end=" ")
    print("*"*i)