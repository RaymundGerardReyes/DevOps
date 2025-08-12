# DevOps
Basic Assessment 

here's intial steps I made start on it Creating my repo using Github repository 

1. basically I initial to create and rename on using 'DevOps' and including add REAMDE.md 

2. the next step on is opening my Git Bash on it, so I basically I save and clone my repo from github on it 'LOQ@RAYMUND-PC03 MINGW64 ~ (main)
$ git clone https://github.com/RaymundGerardReyes/DevOps
Cloning into 'DevOps'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.

'
basically the directory on it was this 'C:\Users\LOQ' 

3. I intially called the folder of the file I clone on it using 'cd' command so basically I named was similar of the repo name I made 
and here's the output 
'LOQ@RAYMUND-PC03 MINGW64 ~ (main)
$ cd DevOps
'
and then I recheck my directory README.md was existed on it so intial to command 
'LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (main)
$ dir
README.md

'

4. next step I need to initialize the git on it so that I can distinguish the history and the github account connected on it using this command 
'LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (main)
$ git init
Reinitialized existing Git repository in C:/Users/LOQ/DevOps/.git/

LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (main)
"

5. I did create a file on it for my code which was basically the suminit.py and I did put simple addition and 

6. Then I did create also for unittest for the suminit.py using unittest.py as for the mean unittest.py so basically I used unittest import libraries for my code unit test

7. after running the test on it, I initially git commit my code suminit.py for my development branch.  

8. I will create 2 branches on it from Development and Staging branch and lastly main branch is for Production
   
9. Basically used this command 
'LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (main)
$ git branch -m Development
' for "Development" branch and next branch for staging branch basically this command 
'LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (Development)
$ git branch -m Staging"


10. Now assuming that I am stilling on code and then unit test for my part development branch so I initially add my suminit.py into Development branch using this command 
'
LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (main)
$ git add suminit.py"

and together with unit test as well after commit message on the sum init

11. step was this commit "LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (Staging)
$ git commit -m "Feature addition" " for suminit.py 
and here's 
"LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (Development)
$ git commit -m "Feature addition"
[Staging a9bb940] Feature addition
 1 file changed, 2 insertions(+)
 create mode 100644 suminit.py"

and then git push on it my Development branch 

"LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (Development)
$ git push origin Development
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 322 bytes | 322.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'Development' on GitHub by visiting:
remote:      https://github.com/RaymundGerardReyes/DevOps/pull/new/Development 
remote:
To https://github.com/RaymundGerardReyes/DevOps
 * [new branch]      Development -> Development
"

12. and For unit test adding and commit message for unittest.py and git push using these commands
'LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (Development)
$ git add unittest.py
'

'LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (Development)
$ git commit -m "Unit test summinit"
[Development 06fe7af] Unit test summinit
 1 file changed, 16 insertions(+)
 create mode 100644 unittest.py

LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (Development)
$ git push origin Development
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 506 bytes | 253.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/RaymundGerardReyes/DevOps
   a9bb940..06fe7af  Development -> Development
'

13. Third step was this Staging branch assuming that it is already for Acceptance testing on it and did this also 
'LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (staging)
$ git commit -m "Acceptance Testing"'

pushing on the Staging branch 

'LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (staging)
$ git push origin Staging
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'Staging' on GitHub by visiting:
remote:      https://github.com/RaymundGerardReyes/DevOps/pull/new/Staging     
remote:
To https://github.com/RaymundGerardReyes/DevOps
 * [new branch]      Staging -> Staging'

14. Assuming that code is ready for production I made to command on this 
'LOQ@RAYMUND-PC03 MINGW64 ~/DevOps
$ git checkout main && git pull origin main
Already on 'main'
Your branch is up to date with 'origin/main'.
From https://github.com/RaymundGerardReyes/DevOps
 * branch            main       -> FETCH_HEAD
Already up to date.
'
and then merging on this 
'LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (main)
$ git merge Staging
Updating e318a59..a9bb940
Fast-forward
 suminit.py | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 suminit.py'

15. Lastly step was this
    'LOQ@RAYMUND-PC03 MINGW64 ~/DevOps (main)
$ git push origin main
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/RaymundGerardReyes/DevOps
   e318a59..a9bb940  main -> main' 








