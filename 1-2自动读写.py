# -*- coding: cp936 -*-

import os
from os.path import join
  
def main() :
    source = "e:\\1\\"
    dest = "e:\\11\\"
    for root, dirs, files in os.walk( source ):
        for OneFileName in files :
            print(OneFileName)
            if OneFileName.find( '.txt' ) == -1 :
                continue
            OneFullFileName = join( root, OneFileName )
            writer = open(dest+OneFileName,'w')
            for line in open( OneFullFileName ):
                writer.write(line+'\n')
            writer.close();
  
if __name__ == "__main__" :
    main()
