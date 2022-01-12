from os import system as t

t("rm .git*")
t("git init")
t("git add .")
t(r'git commit -m "first commit" ')

t("git push -u origin master")