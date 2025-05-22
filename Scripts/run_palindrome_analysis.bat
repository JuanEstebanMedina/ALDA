@echo off
call .\env\Scripts\activate
@REM python -m algorithm_analysis.app --experiment palindrome --sizes "100 1001 10 15"
@REM python -m algorithm_analysis.app --experiment palindrome --sizes "10000 100001 500 15"
python -m algorithm_analysis.app --experiment palindrome --sizes "1000 5000 10 3"


