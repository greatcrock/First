"""
You are given a list of files. You need to sort this list by the file extension. The files with the same extension should be sorted by name.

Some possible cases:

Filename cannot be an empty string;
Files without the extension should go before the files with one;
Filename ".config" has an empty extension and a name ".config";
Filename "config." has an empty extension and a name "config.";
Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
Filename ".imp.xls" has an extension "xls" and a name ".imp".

Input: A list of filenames.
Output: A list of filenames.
"""

from typing import List

def personal(elem):
    q = elem.split(".")
    if q[0] == "" and len(q) == 2:
        back = q[0] + "." + q[1]
    elif len(q) == 3:
        back = q[-1] + "." + q[0] + "." + q[1]
    else:
        back = q[1] + "." + q[0]
    return back

def sort_by_ext(files: List[str]) -> List[str]:
    # your code here
    return sorted(files, key=personal)

    # for i in a:
    #     k = i[0]
    #     v = i[-1]
    #     pain[k] = v
    #     print(k, v)
    # m = sorted([(v, k) for k,v in pain.items()])
    # print(m)
    # m = [(str(k) + str(v)) for v, k in m]

print(sort_by_ext(['1.cad', '1.bat', '1.aa', ".ff.bb"]))
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']))
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad'])
print("Itself", sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']))

# These "asserts" are used for self-checking and not for an auto-testing
print(1,sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad'])
print(2,sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad'])
print(3,sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad'])
print(4,sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad'])
# assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
print(5,sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc'])
print(6,sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc'])
print(6,sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']))
print(7,sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']))
print(sort_by_ext([".config","my.doc","1.exe","345.bin","green.bat","format.c","no.name.","best.test.exe"]) == [".config","no.name.","green.bat","345.bin","format.c","my.doc","1.exe","best.test.exe"])
print(sort_by_ext([".config","my.doc","1.exe","345.bin","green.bat","format.c","no.name.","best.test.exe"]))