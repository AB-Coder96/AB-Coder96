python ExceltoWord.py
python WordtoHTML.py
setlocal enabledelayedexpansion
for /f "tokens=*" %%a in ('hostname') do set "computer_name=%%a"
git submodule foreach 'git stash'
Git add .
Git commit -m "manual web updates (!computer_name!)"
git push --force
endlocal
pause
