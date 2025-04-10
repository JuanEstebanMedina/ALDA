@echo off
call .\env\Scripts\activate
python -m algorithm_analysis.app --experiment searching --sizes "1000000 30000001 1000000 7"