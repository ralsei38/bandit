import asyncio
import asyncssh
import sys

port = 2220
server = "bandit.labs.overthewire.org"


async def run_client(name, passwd, cmd):
    async with asyncssh.connect(
        server, username=name, password=passwd, port=port
    ) as conn:
        result = await conn.run(cmd, check=True)
        return result


bandit_passwords = ["bandit0"]
cmds = [
    "cat readme",
    "cat ./-",
    "cat 'spaces in this filename'",
    "cat ~/inhere/.hidden",
    "cat ~/inhere/-file07",
    "cat $(find ~/inhere/* -size 1033c)",
    "cat $(find / -group bandit6 -user bandit7 2>/dev/null)",
    "cat data.txt |grep millionth | awk '{print $2}'",
    "sort ~/data.txt | uniq -u",
    "strings ~/data.txt |grep '&==' | awk '{print $2}'",
]

try:
    for i in range(0, (len(cmds))):
        username = "bandit" + str(i)
        result = asyncio.get_event_loop().run_until_complete(
            run_client(username, bandit_passwords[i], cmds[i])
        )
        bandit_passwords.append(result.stdout.strip())
        print(f" level {i} passed, password: {result.stdout.strip()}")

except (OSError, asyncssh.Error) as exc:
    sys.exit("SSH connection failed: " + str(exc))
