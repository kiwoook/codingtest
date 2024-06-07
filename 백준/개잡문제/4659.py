import sys

vowel = ['a', 'e', 'i', 'o', 'u']


def check1(s):
    for char in s:
        if char in vowel:
            return True

    return False


def check2(s):
    cnt_vowel = 0
    cnt_consonant = 0

    for char in s:
        if char in vowel:
            cnt_vowel += 1
            cnt_consonant = 0
            if cnt_vowel >= 3:
                return False
        else:
            cnt_consonant += 1
            cnt_vowel = 0
            if cnt_consonant >= 3:
                return False

    return True


def check3(s):
    for i in range(len(s) - 1):
        if s[i] == 'e' or s[i] == 'o':
            continue
        if s[i] == s[i + 1]:
            return False

    return True


cmd = sys.stdin.readline().rstrip()

while cmd != 'end':
    # 1번 조건
    sw = 0
    if not check1(cmd):
        sw = 1
    if not check2(cmd):
        sw = 1
    if not check3(cmd):
        sw = 1

    if sw == 1:
        print("<" + cmd + ">" + " is not acceptable.")
    else:
        print("<" + cmd + ">" + " is acceptable.")

    cmd = sys.stdin.readline().rstrip()
