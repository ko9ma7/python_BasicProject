@echo off
color 0a
mode 200
title  wifi infomation by noski
cls

:YES
echo "wifi list�� Ȯ���Ͻðڽ��ϱ�?"
set /p select=(Y/N):
if "%select%"=="N" exit
rem md C:\ProgramData\info.txt
netsh wlan show profiles name=* > "C:\ProgramData\info.txt"
find "SSID �̸�" "C:\ProgramData\info.txt"
::
set /p wifiname=�˻��� �������� �̸�:
::
netsh wlan show profiles name=%wifiname% key=clear > "C:\ProgramData\info.txt"
::
echo "==========confirm=========="
find "Ű ������" "C:\ProgramData\info.txt"
::
if "%wifiname%"=="0" exit
goto YES