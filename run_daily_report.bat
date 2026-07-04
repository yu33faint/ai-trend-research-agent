@echo off
chcp 65001 > nul
cd /d C:\dev\ai-trend-research-agent

if not exist logs mkdir logs

set PYTHONUTF8=1
.\.venv\Scripts\python.exe -X utf8 main.py >> logs\daily_report.log 2>&1