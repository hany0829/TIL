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