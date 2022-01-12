from os import system as t

t("rm .git*")
t("git init")
t("git add .")
t("git remote set-url origin https://github.com/guilipeh-git/-whatsapp_bot_gui.git")
t(r'git commit -m "first commit" ')

t("git push -u origin master")