# bandit
automating the resolution of bandit challenges from https://overthewire.org/wargames/bandit/

## Exercice 0

Les identifiants du premier challenge sont donnée sur la page, les paramètres de connexion aussi:

```bash
username: bandit0
password: bandit0
host: bandit.labs.overthewire.org
port: 2220
```

### Solution 0

```bash
cat readme
#boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

### Solution 1

```bash
cat ./-
#CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```



### Solution 2

```bash
cat 'spaces in this filename'
#UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```



### Solution 3

```bash
cat ~/inhere/.hidden
#UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```




### Solution 4

```bash
find ~/inhere/ | xargs file
```

```bash
.:         directory
./-file01: data
./-file00: data
./-file06: data
./-file03: data
./-file05: data
./-file08: data
./-file04: data
./-file07: ASCII text
./-file02: data
./-file09: data
```

```bash
cat ~/inhere/-file07
#koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

### Solution 5

```bash
cat $(find ~/inhere/* -size 1033c)
#DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

### Solution 6

```bash
cat $(find / -group bandit6 -user bandit7 2>/dev/null)
#HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

### Solution 7

```bash
cat data.txt |grep millionth | awk {print $2}
#cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

### Solution 8

```bash
sort ~/data.txt | uniq -u
# UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```



### Solution 9

```bash
bandit9@bandit:~$ strings ~/data.txt |grep '=='
========== the*2i"4
========== password
Z)========== is
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
#pour récupérer précisemment cette ligne
strings ~/data.txt |grep '&==' | awk '{print $2}'
```

