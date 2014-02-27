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
    __perLen=0
    def reporthook(a, b, c):    # a:已经下载的数据大小; b:数据大小; c:远程文件大小;
        if c > 1000000:
            nonlocal __perLen
            per = (100.0 * a * b) / c
            if per>100: per=100
            per = '{:.2f}%'.format(per)
            print('\b'*__perLen, per, end='')     # 打印下载进度百分比
            sys.stdout.flush()
            __perLen = len(per)+1
    urllib.request.urlretrieve(mlink, mname+'.mp3', reporthook)
main() #Entry
