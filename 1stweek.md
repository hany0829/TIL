># 12/26
Git : `분산` `버전` `관리` 시스템

    1. 작업을 하고
    2. 변경된 파일을 모아 add
    3. 버전으로 남긴다 commit

- Working Directory(1통)
     
     파일의 변경사항 Working Tree clean
- staging area(2통)

    버전으로 기록하기 위한 파일 변경사항의 목록 / nothing to commit
repository 

    커밋들이 기록되는 곳

- Working Tree clearn nothing to commit → 1통 2통 비어있음



- git config --global user.email "hany8092@naver.com"    
- git config --global user.name "hany0829"


># 12/27 **복습** 
    git 사용순서
    git init - git status - git add 파일명 - git status - git commit -m ''

    - 커밋해쉬값 : 고유한 번호
    - head - master 브랜치 : 나의 위치

    - .git 폴더를 지워도 된다? X
    - 폴더 이름 바꿔도 된다? O
    - 다른곳으로 폴더로 이동시켜도 된다? △ : 다른 폴더에 git 중첩 되면 안되기 떄문에이다.

># 12/28 **학습 목표**

    - 원격저장소 활용 명령어를 이해하고 설명 할 수 있다.
    - 분산버전관리시스템을 이해하고 설명할 수 있다.
___
<br>

- `Git,GitHub`는 `버전`을 `관리`한다.

- `Push` : 로컬 저장소의 버전을 원격저장소로 보낸다.

- `Pull` : 원격저장소의 버전을 로컬 저장소로 가져온다.

- git / remote / add / origin https://github.com/hany0829/test.git //
 
  원격저장소 / 추가 / orgin으로 / GitHub user name/ 저장소 이름 //

-  `git add` 한 후에 `git commit`를 반드시 해야만 원격저장소에 저장됩니다.

- $ git push / pull origin master

- 2명이서 작업 할 때는 `push pull` 하지만 제3자가 가져올 때는 `clone`을 이용한다.

- 다운로드와 clone의 차이
    
    다운로드 : (가장 최신 버전의 상태의) 파일만 받는 것이다.
    
    clone : git 저장소를 받아오는 것 모든 버전을 받은 것이다.


- ~~git clone 한 다음에 init 할 필요X~~

- 충돌하면 GitHub이랑 비교해서 원격저장소의 커밋을 pull 해서 다시 push 하면 병합됩니다.
- VScode에서 파일옆에 의미하는 뜻

    u : untracted

    m : modified

- .ignore : git으로 관리하지 않을 파일들을 미리 지정해서 헷갈리지 않게 해줍니다. `.ignore 자체가 파일`입니다.
→[참조](https://www.toptal.com/developers/gitignore/)

- bash 창에서 `git config --global core.editor "code --wait"` :  커밋메세지 길게 하고 싶을 때 사용합니다.
<br>
<br>
>## **명령어 정리**
<br>

- git clone <url> : 원격 저장소 복제

- git remote -v : 원격저장소 정보 확인

- git remote add <원격저장소> <url> : 원격저장소 추가(일반적으로 origin)

- git remote rm <원격저장소> : 원격저장소 삭제

- git push <원격저장소> <브랜치> : 원격저장소에 push

- git pull <원격저장소> <브랜치> : 원격저장소로부터 pull


># Branch 
- 독립적인 작업흐름을 만들고 관리

>## **브랜치 주요 명령어**

1. 브랜치 생성 :
(master) $ git branch {branch name}
2. 브랜치 이동 :
(master) $ git checkout {branch name}
3. 브랜치 생성 및 이동 :
(master) $ git checkout -b {branch name}
4. 브랜치 목록 :
(master) $ git branch
5. 브랜치 삭제 :
(master) $ git branch -d {branch name}

<br>

>## Merge
- 각 branch에서 작업을 한 이후 이력을 합치기 위해 사용
- 병합을 진행할 때, 서로 다른 commit에서
    - 이 경우에는 반드시 직접 해당 파일을 확인하고 적절히 수정
    - 수정한 이후에 직접 commit 실행
- 다른 파일을 수정한 경우
    - 충돌 없이 자동으로 Merge Commit이 생성됨


> ## **GitHub Flow 기본원칙**


1. 브랜치 만들고
2. 작업
3. 커밋
4. 로컬에서 master 이동 후 병합 (제일 중요)

>### **참고**
- a.txt 파일만 커밋하려고 했는데 git add . 해버렸을 때

    git restore --staged <file>

    restore(1통) / restore --staged(2통)

- `commit 메세지` 바꾸는 것 `유의` (해쉬값이 다름) 원격으로 보내기전까진 가능 push 한 이후로는 `불가능`