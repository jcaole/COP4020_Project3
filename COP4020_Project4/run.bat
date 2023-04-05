@echo off
echo --------------START--------------

echo Running program with legal1.txt
python fsa.py fsa.txt legal1.txt

echo Running program with illegal1.txt
python fsa.py fsa.txt illegal1.txt


echo --------------DONE--------------