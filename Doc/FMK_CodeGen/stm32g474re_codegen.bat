@echo off
REM Spécifiez le chemin vers l'exécutable Python si nécessaire
set PYTHON_PATH=python

cd /d %~dp0\..\..

REM Exécuter le script Python avec des arguments fixes
%PYTHON_PATH% Doc\FMK_CodeGen\Script\main.py Doc\FMK_CodeGen\Cfg\STM32G474RE\STM32G474RE_HwCfg.xlsx

echo Press any key to continue...
pause