@echo off
call .\env\Scripts\activate
python -m algorithm_analysis.app --experiment sorting --sizes "1000 6001 1000 7"