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
```

### Solution 1

```bash
cat ./-
```



### Solution 2

```bash
cat 'spaces in this filename'
```



### Solution 3

```bash
cat .hidden
```



### Solution 4

```bash
cat .hidden
```



### Solution 5

```bash
find . | xargs file
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
cat ./-file07
```
