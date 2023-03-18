@echo off
echo --------------START--------------

echo --------------Running program with legal1.txt--------------
py fsa.py fsa.txt legal1.txt

REM --------------echo Running program with legal1.txt--------------
REM py fsa.py testfsa.txt legal1.txt

REM --------------echo Running program with legal1.txt--------------
REM py fsa.py testfsa2.txt legal1.txt

echo --------------Running program with illegal1.txt--------------
py fsa.py fsa.txt illegal1.txt

REM --------------echo Running program with illegal1.txt--------------
REM py fsa.py testfsa.txt illegal1.txt

REM --------------echo Running program with illegal1.txt--------------
REM py fsa.py testfsa2.txt illegal1.txt


echo --------------DONE--------------