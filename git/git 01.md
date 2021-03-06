# git day 1

## GIT

특정 파일을 관리하는게 아니라 `폴더`를 관리하는 툴

리포 = 업그레이드 된 폴더

리포로 업그레이드하면 하위 폴더는 자동으로 관리가 들어감

파란색(`master`)이 붙어있으면 리포(저장소), 없으면 폴더

`ctrl + l` : 화면 클리어

`q`  : log가 길어서 안넘어갈때

**commits** 사진

- `git init` : 폴더를 리포로 업그레이드

- `rm -r .git` : 다운그레이드

- `git status` : 현재 상황

- `touch README.md` : 새파일 생성

- `git add README.md` : 
- `git commit -m 'first commit'` : git에서 메모(-m)를 남길거야 '이러한내용' 으로 
  - 첫번째 커밋이 중요해요

- `git config --global user.name '내이름'`

- `git config --global user.email '이메일@주소'`
- 다시 `git commit -m 'first commit'` 입력해야 커밋생성됨
- `git log` : 커밋 확인



```
# 초기화 할때 1회 입력
git init
```

```
# 계속 쓸 명령어
git add filename
git commit -m 'MESSAGE'
```

```
git status
git log
```



파일을 메이크업 시켜서 스테이지에 올려서 촬영

파일 메이크업 = 코드 작성

스테이지에 올리는 명령어 git add

사진 촬영 = commit

스테이지에서 촬영한 사진이 사진첩으로 가면, 사진 목록을 보는 명령어 git log

파일이 지금 어디에 있는지 확인하는 명령어 git stauts

스테이지에서 내리려면 git restore --staged filename

더 예전 사진으로 가려면 git restore  filename

| 분장실      | 스테이지 | 사진첩 |
| ----------- | -------- | ------ |
| 여기가 메인 |          |        |

빨간색 글씨  : 스테이지에 안올라가서 커밋안됨

초록색 글씨 : 변경사항 커밋된다



방금 생성된 파일들은 untracked, 모르는 사람들 

얼굴도장을 찍는다 = 스테이지에 한번이라도 올라감

`git add .` : 내 위치에 있는 모든 파일을 add

변경사항이 없으면 add해도 스테이징 안됨

커밋하면 사진에 메모가 추가되는 것



**NEVER**

1. 홈폴더(`~`)에서 초기화(`git init`)
2. 리포안에 리포
3. `git init` 입력 전 확인할 점
   1. `~`인지
   2. (`master`) 떠있는지

### github

1. 깃허브에 매칭되는 리포를 만들고 (생성된 주소 복사하기)

2. 내컴퓨터의 리포 폴더를 동기화

3. 가지고있는 커밋을 깃허브에 옮기기
   
`git remote add <name> <URL>` : add까지는 고정값, name부터는 고정값이 아니고 딕셔너리로 생각 {origin : <URL>}

`git remote remove <name>` : <name> 값 삭제

`git push <name> master` : push까지는 고정값



## Git-Bash

### 명령어

- `touch 파일명.확장자` : 파일 생성
- `mkdir 폴더명 ` : 폴더 생성
- `mv 파일명.확장자 폴더명/` : 폴더로 파일 옮기기
- `cd 폴더명` : 폴더로 들어가기
- `ls` : 지금 위치한 폴더의 내용 보여줌
-  `cd ..` : 상위 폴더로 올라감
- `cd` : 홈폴더로 돌아감
- `rm 파일명.확장자` : 파일 제거 (영구삭제)
- `rm *.확장자` : 폴더의 모든 파일 삭제 (`* ` : 모든 값 )
- `touch .파일명.확장자` : 숨겨진 파일 생성 (윈도우에서는 볼수있음)
- `ls -a` : 숨겨진 파일 확인 (`./` : 지금 위치한 폴더, `../` : 상위폴더)
- `rm -r 폴더명` : 폴더 제거
- `code .` : 지금 위치한 폴더를 vscode로 열어줌 

## VSCode

## Typora

- `#` : 제목
  -  `#` ~ `######` 까지 가능
- `*텍스트*` : 기울어진 텍스트
-  `-` : 순서 없는 목록
- `1.` : 순서 있는 목록
- `**텍스트**` : 볼드체
- \`\` : lnline code
- \`\`\` : 함수 작성, 언어 설정, 작성이 끝나면 `crtl + enter`
- `|하나|둘|셋|` : 표 작성, 추가로 작성을 하려면 `crtl + enter`
- `\` : 문자열 이스케이프, 역슬래시 + 쓰려는 문자

