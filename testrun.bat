@echo off
echo --------------START--------------

REM echo Running program with testlegal1.txt
REM py fsa.py fsa.txt testlegal1.txt

REM echo Running program with testlegal2.txt
REM py fsa.py fsa.txt testlegal2.txt

echo Running program with legal1.txt
py fsa.py fsa.txt legal1.txt


REM echo Running program with testfsa.txt and legal1.txt--------------
REM py fsa.py testfsa.txt legal1.txt

echo Running program with testfsa2.txt legal1.txt--------------
py fsa.py testfsa2.txt legal1.txt


REM echo Running program with illegal1.txt
REM py fsa.py fsa.txt illegal1.txt

REM echo Running program with testfsa.txt and testlegal3.txt
REM py fsa.py testfsa.txt testlegal3.txt

echo Running program with testfsa2.txt and testlegal3.txt
py fsa.py testfsa2.txt testlegal3.txt

REM echo Running program with illegal1.txt--------------
REM py fsa.py testfsa.txt illegal1.txt

REM --------------echo Running program with illegal1.txt--------------
REM py fsa.py testfsa2.txt illegal1.txt


echo --------------DONE--------------