@echo off
cd /d C:\Users\yomak\OneDrive\Desktop\python\stud-pract\Python\works\16\task2

start cmd /k py server.py
timeout /t 2 > nul
start cmd /k py client.py