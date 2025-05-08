---
title: Git Secret
---

[make a new key](/notebook/ssh/gpg-reference/) for my_email@emailaddress.com

```bash
git secret init
echo "this is my secret" >> my_secret.txt
echo "my_secret.txt" >> .gitignore
#git secret tell <email address>
# for example,
git secret tell my_email@emailaddress.com
git secret add my_secret.txt
git secret hide
git add .gitignore .gitsecret/ my_secret.txt.secret 
git commit -m "test"
git push
```

when you clone to a new computer

[load your keys](/notebook/ssh/gpg-reference/)

reveal your secrets

```bash
git secret reveal
```


## External Resources

* <https://dev.to/vnjogani/a-guide-to-git-secret-49g3>
* for larger teams: <https://github.com/getsops/sops>