# git commmit
 - 要关联一个远程库，使用命令git remote add origin git@server-name:path/repo-name.git；
 - 关联一个远程库时必须给远程库指定一个名字，origin是默认习惯命名；
 - 关联后，使用命令git push -u origin master第一次推送master分支的所有内容；
 - 此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；


# create
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/zzzzlalala/github.git
- git push -u origin main


# push
- git remote add origin https://github.com/zzzzlalala/github.git
- git branch -M main
- git push -u origin main
  
### 参考链接
https://segmentfault.com/u/mataotao/articles?page=4