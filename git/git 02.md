# git day 2

- 폴더 만들고(`mkdir`) -> 폴더로 이동(`cd`) -> 폴더를 리포로 초기화(`git init`) -> 파일생성(`touch README.md .gitignore`) -> 파일add(`git add .`)  -> 커밋(`git commit`)

- 깃허브에 원격 저장소 생성하고
  - 생성하고 주소 복사하기
- 원격저장소(remote repo)에 추가
  - `git remote add <name> <URL>`
- 원격 저장소 확인
  - `git remote -v`

- 원격 저장소에 지금까지의 커밋들 push
  - ​	`git push origin master`



- `git remote -h` : help, 쓸수있는 명령어 확인 가능

- `git remote add <name> <URL>` : add까지는 고정값, name부터는 고정값이 아니고 딕셔너리로 생각 {origin : <URL>}

- `git remote remove <name>` : <name> 값 삭제

- `git push <name> master` : push까지는 고정값



- `git log --oneline`  : 간략하게 커밋 확인

```
$ git log --oneline
831f468 (HEAD -> master) CLI.md 생성 및 git 내용 추가
85b1516 (origin/master) first commit

- remote에는 (origin/master)까지만 들어갔고, 최신은 (HEAD->master) 이다
	- push를 하면 동기화됨 -> (HEAD -> master, origin/master) 이렇게 나옴
```

- 비어있는 폴더는 커밋해도 안올라감, 없는걸로 생각..

- 새로운 컴퓨터에서 기존 원격 저장소 복제하기
  ```sh
  $ git clone <URL>
  ```
- 원격 저장소의 내용 받아오기
  ```sh
  $ git pull origin master
  ```


- 모든 프로젝트는 기본으로 `README.md` 와 `.gitignore`은 무조건 있어야함
  - `.gitignore` : 이 프로젝트에서 제외할 파일이 있을때, 무시할 파일명을 ignore에 추가하면 됨
  - 구글에 `gitignore.io` 검색해서 쓰고있는 프로그램을 추가하면 무시할 파일들을 알려줌, 모두 복사에서 `.gitignore`에 붙여넣기
  - 깃 초기화 전에 작성해주는게 좋아요



## 충돌

### 두 개의 컴퓨터에서 작업

A에서 커밋 후 `push`를 한 뒤, A에서 수정을 하고 커밋을 하지 않았다.

B에서 `git clone`을 이용해 `pull`을 하여 작업 뒤 수정된 파일을 커밋 후 `push`로 `remote` 하였다.

A에서 다시 pull을 하려는데 현재 A에서 수정된 파일과 pull 하려는 파일의 내용이 달라서 오류가 난다.

- 해결방법

  1. 다른 파일인 경우
     - A에서 뒤늦게 커밋 후 `push`하려니 안됨
     - 먼저 `remote`에서 `pull`을 한 뒤
     - `push`하면 자동으로 병합하여 변경해줌

  2. 같은 파일이지만 다른 위치에서 변경됨
     - 위와 같은 방법
  3. 같은 파일, 같은 위치
     - 위의 방법으로 해결되지 않는다
     - 자동 병합이 안되고 직접해야함
     - 파일에서 어떤 내용을 살릴지 선택하고 커밋, `push`



## branch

`(master)` : branch 이름,  브랜치(=화살표)

- `git branch <name>` : 새로운 브랜치 생성
- `git branch -d <name>` : 브랜치 제거
- `git switch <branch name>` : 다른 브랜치로 이동
- `git switch -c <branch name>`
- `git merge <branch name>` : 다른 브랜치와 병합, master에서 해야함

마스터 - 동작하는 프로그램, 마스터 시점의 커밋을 출시

브랜치가 없으면 조금씩 수정할때마다 출시를 해야해
브랜치로 계속 가다가 언젠가는 마스터가 됨 (merge)
브랜치 망하면 잘라버리면됨
병합하려면 일단 마스터로 옮겨가서, `master`가 b1을 병합

- 병합 방법 :  `git merge <branch name>`
1. Fast Forward
   - 화살표를 옮기기 숟가락 얹기..
2. Auto Merge
   - 마스터를 수정한 다음 브랜치와 병합 후 커밋
3. 파일이 겹칠때
   - 위의 충돌할때 처럼 파일 직접 수정 후 커밋



### 협업

먼저, `remote`에서 리포 생성한뒤, 

`git clone <URL>` 로 가져옴

그 뒤 각자 리포에서 브랜치를 먼저 만들고 작업 (`git switch -c <branch name>`)

작업한뒤 push할때 -> `git push origin <branch name>` 으로 해야함

`remote`에서 pull request 생성

최종 merge 결정(Auto or Conflict(직접 수정 필요))

로컬 `master`에서 `git pull origin master`

반복
