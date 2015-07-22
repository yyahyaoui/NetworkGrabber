import crypt
import os
import sys



def check_file(filename):
    if not os.path.isfile(filename):
        print "[-] file name %s don't exist" % str(filename)
        exit(0)
    if not os.access(filename, os.R_OK):
        print "[-] access denied for filename %s" % str(filename)
        exit(0)

def main():
    if(len(sys.argv) == 3):
        pwd_filename = sys.argv[1]
        dict_filename = sys.argv[2]
        check_file(pwd_filename)
        check_file(dict_filename)
    else:
        print "Usage: python %s <passswd.txt> <dictionnary.txt>" %str(sys.argv[0])
        exit(0)
    
    try:
        f = open(pwd_filename, 'r')
        for line in f.readlines():
            splits = line.strip('\n').split(':')
            if (len(splits) > 1):
                user = splits[0]
                hashPsw = splits[1].strip(' ')
                print "Trying to crack password for user %s" %str(user)
                g = open(dict_filename, 'r')
                testPass(hashPsw, g.readlines())
    except Exception,e:
        print "An exception occured while trying to read file %s: %s" %(str(pwd_filename), str(e))
         

def testPass(crypPass , lines):
    salt = crypPass[0:2]
    for line in lines:
        if (crypPass == crypt.crypt(str(line.strip('\n')), salt)):
            print "Crack successful : Password found in Dictionnary! Crack is : %s" %str(line.strip('\n'))
    
    
    
''' main start '''    
if __name__ == '__main__':
        main()