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
  - 구글에 gitignore 검색해서 쓰고있는 프로그램을 추가하면 무시할 파일들을 알려줌, 모두 복사에서 `.gitignore`에 붙여넣기
  - 깃 초기화 전에 작성해주는게 좋아요