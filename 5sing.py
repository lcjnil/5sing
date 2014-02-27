import urllib.request
import sys, getopt
import re
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "l:h", ["help"])
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit()
            elif opt in ("-l"):
                fk5sing(arg)
    except getopt.GetoptError:
        usage()

def usage():
    print("-h Help")
    print("-l Link")

def fk5sing(link):
    content=urllib.request.urlopen(link).read()
    content=content.decode("utf8")
    pat = re.compile(r'file: "(.*?)"')
    pat2 = re.compile(r'var SongName   = "(.*?)";')
    mlink = pat.findall(content)[0]
    mname = pat2.findall(content)[0]
    urllib.request.urlretrieve(mlink, mname+'.mp3')

main()
