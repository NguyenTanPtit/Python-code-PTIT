# PYTHON FILE
s = input()
if s[len(s)-3::] == '.py' or s[len(s)-3::] == '.PY' or s[len(s)-3::] == '.Py' or s[len(s)-3::] == '.pY':
    print('yes')
else:
    print('no')
