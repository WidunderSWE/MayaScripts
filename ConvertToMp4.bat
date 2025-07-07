@echo off
setlocal EnableDelayedExpansion
title Convert Videos to MP4 (With Audio)

:: Path to ffmpeg
set "ffmpeg_exe=C:\ffmpeg.exe"
if not exist "%ffmpeg_exe%" (
    echo ❌ ffmpeg.exe not found at %ffmpeg_exe%
    pause
    exit /b
)

:: Supported extensions
set "exts=avi mov mkv mp4 wmv webm m4v mpg mpeg"

:: Default to current folder if no args
if "%~1"=="" (
    set "mode=folder"
    set "input_folder=%~dp0"
    goto :process_folder
)

:: Process each drag-and-drop target
:loop
if "%~1"=="" goto :end

if exist "%~1\" (
    call :process_folder "%~1"
) else (
    call :process_file "%~1"
)
shift
goto :loop

:process_folder
set "folder=%~1"
set "folder=%folder:"=%"
for %%F in ("%folder%\*.*") do (
    call :process_file "%%~fF"
)
goto :eof

:process_file
set "filepath=%~1"
set "filepath=%filepath:"=%"
set "ext=%~x1"
set "ext=%ext:~1%"
set "filename=%~nx1"
set "nameonly=%~n1"
set "outdir=%~dp1converted_mp4"
for %%E in (%exts%) do (
    if /I "%ext%"=="%%E" (
        if not exist "%outdir%" mkdir "%outdir%"
        echo 🎧 Converting: %filename%
        "%ffmpeg_exe%" -i "%filepath%" -c:v libx264 -preset slow -crf 23 -c:a aac -b:a 192k "%outdir%\%nameonly%.mp4"
    )
)
goto :eof

:end
echo.
echo ✅ Done! MP4s saved in 'converted_mp4' folders
pause
