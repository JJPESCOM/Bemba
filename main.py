import os
import random
from datetime import date, time, datetime
import datetime
# https://github.com/JJPESCOM/OpenAI.git
# https://github.com/JJPESCOM/Turkish_STT.git
# https://github.com/JJPESCOM/Bemba.git
total_day = 300 #total days back
commit_frequency = 8 #commit time per day
repo_link = "https://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@github.com/JJPESCOM/Bemba.git"
pointer = 365

tl = total_day #time day
ctr = 1

now = datetime.datetime.now()

f = open("commit.txt", "w")
# os.system("cd Turkish-Speech-to-Text")
os.system("git init")
os.system("git config user.name \"JJPESCOM\"")
os.system("git config user.email \"jjpes89.dev@outlook.com\"")


def randtime(start_time = datetime.time(9, 0, 0), end_time = datetime.time(17, 0, 0)):
    time_range = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(datetime.date.today(), start_time)
    random_seconds = random.randint(0, time_range.seconds)
    return (
        datetime.datetime.combine(datetime.date.today(), start_time)
        + datetime.timedelta(seconds=random_seconds)
    ).time()

while tl > 0:
    ct = random.randint(0, 6)
    while ct > 0 and random.randint(0,2):
        with open("commit.txt", "a+") as f:
            l_date = now + datetime.timedelta(days=-pointer)
            if l_date.weekday() == 5 and random.randint(0, 7) != 5:
                break
            if l_date.weekday() == 6 and random.randint(0, 12) != 5:
                break
            formatdate = l_date.strftime("%Y-%m-%d")
            formattime = randtime()
            f.write(f"commit ke {ctr}: {formatdate}\n")
        os.system("git add .")
        os.system(f"git commit --date=\"{formatdate} {formattime}\" -m \"commit ke {ctr}\"")
        print(f"commit ke {ctr}: {formatdate}")
        ct-=1
        ctr+=1
    pointer+=1
    tl-=1

os.system(f"git remote add origin {repo_link}")
os.system(f"git remote set-url origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")