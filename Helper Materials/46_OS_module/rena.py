def rename( a  , b):
    import os
    for i in range(int(b)):
         os.rename(f'{a}/fill{i}' , f'{a}/file {i+1}')