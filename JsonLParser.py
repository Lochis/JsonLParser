# packages
import json

# parse JSONL with indentations
def parse(filename, destinationFile, value):
    # list of items
    printLine = ""
    printArr = []
    cnt=0;

    # open JSONL file
    print("\nopening input file...\n")
    with open(filename, 'r') as f:
            print("find keys, push to array...")
            for i in range(1000000):
                #read line from file
                data = f.readline()
                
                data = data.split(' ')
                
                #find all keys
                found = filter(lambda a: '\"' + value + '\":' in a, enumerate(data))\
                    
                #assign keys to var    
                firstKeys = list(found)
                
                #get rid of the []
                foundKeys = [ele for ele in firstKeys if ele != []]
                
                arr = []
                cnt=0
                
                #iterate through keys and push it to an array
                for i in foundKeys: 
                    arr.append(foundKeys[0][0])    
                    
                    for j in arr:
                        # remove chars from line
                        printLine = data[j+1].replace('"', '')
                        printLine = printLine.replace(',', '')
                    if cnt <= 0:
                        printArr.append(printLine)
                        #print(printLine)  used to print each to console.. just put it to file now
                        cnt+=1
            print("done pushing, closing input file")
                        
    f.close()
    
    print("opening destination file...")
    #put lines to file
    with open(destinationFile, 'w') as d:
        for a in printArr:
            d.write("%s\n" % a)
            
    print("wrote to destination file...gg")        
            
    d.close()        
                              
# go
if __name__ == '__main__':
    # call parse
    data = parse('C:\\input file.jsonL', 'E:\\destination file.txt', 'expanded')
    