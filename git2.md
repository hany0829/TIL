
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

- `git pull <원격저장소> <브랜치> : 원격저장소로부터 pull


