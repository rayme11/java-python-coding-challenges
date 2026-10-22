@echo off
REM Phase 2 test runner. Usage:
REM   run-tests.bat                    - run all test suites
REM   run-tests.bat api                - run API tests only
REM   run-tests.bat web                - run Selenium web tests only
REM   run-tests.bat stability          - run stability/retry tests only
REM   run-tests.bat playwright         - run Playwright example (visible browser)
REM   run-tests.bat selenium-example   - run Selenium example (visible browser)

setlocal enabledelayedexpansion
set JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-25.0.4.101-hotspot
set MVN=C:\tools\Maven\apache-maven-3.9.6\bin\mvn.cmd
cd /d "%~dp0"

set SUITE=%~1
echo DEBUG: Initial SUITE=[%SUITE%]
if "%SUITE%"=="" set SUITE=all
echo DEBUG: Processed SUITE=[%SUITE%]

if /i "%SUITE%"=="api" (
    echo === Running API tests [REST Assured] ===
    call "%MVN%" test -Dtest=enterprise.qe.api.ApiTest
    goto :eof
)

if /i "%SUITE%"=="web" (
    echo === Running Web tests [Selenium, visible Chrome] ===
    call "%MVN%" test -Dtest=enterprise.qe.web.WebTest
    goto :eof
)

if /i "%SUITE%"=="stability" (
    echo === Running Stability tests [retry logic] ===
    call "%MVN%" test -Dtest=enterprise.qe.stability.StabilityTest
    goto :eof
)

if /i "%SUITE%"=="playwright" (
    echo === Running Playwright example [visible Chromium] ===
    call "%MVN%" org.codehaus.mojo:exec-maven-plugin:3.6.4:java -Dexec.mainClass=enterprise.qe.web.PlaywrightExample
    goto :eof
)

if /i "%SUITE%"=="selenium-example" (
    echo === Running Selenium example [visible Chrome] ===
    call "%MVN%" org.codehaus.mojo:exec-maven-plugin:3.6.4:java -Dexec.mainClass=enterprise.qe.web.WebAutomationExample
    goto :eof
)

if /i "%SUITE%"=="all" (
    echo === Running ALL test suites ===
    call "%MVN%" clean test
    goto :eof
)

echo Unknown suite: %SUITE%
echo Valid: all, api, web, stability, playwright, selenium-example
exit /b 1