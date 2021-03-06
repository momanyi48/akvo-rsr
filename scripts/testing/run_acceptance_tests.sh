#!/bin/bash

# Parameters:
# $1: acceptance_test_project_name
# $2: rc_server_log_path
# $3: xvfb_log_path (optional)


function display_usage_and_exit
{
    echo "Usage: run_acceptance_tests <acceptance_test_project_name> <rc_server_log_path> [xvfb_log_path]"
    echo "Optionally specify an xvfb_log_path to run tests in headless mode"
    exit -1
}

function verify_script_parameters
{
    # warn if extraneous parameters exist
    if [ -n "$4" ]; then
        echo ">> Unexpected number of parameters: $*"
        display_usage_and_exit
    fi

    # check if acceptance_test_project_name parameter exists
    # tests are expected in the tests/PROJECT_NAME/acceptance directory
    if [ -z "$1" ]; then
        echo ">> Missing acceptance_test_project_name parameter (e.g. akvo)"
        display_usage_and_exit
    fi

    # check if rc_server_log_path parameter exists
    if [ -z "$2" ]; then
        echo ">> Missing rc_server_log_path parameter"
        display_usage_and_exit
    fi
}

function set_python_path_for_acceptance_tests
{
    # check if PYTHONPATH exists
    if [ -z "$PYTHONPATH" ]; then
        export PYTHONPATH="$ACCEPTANCE_TEST_ROOT_DIR"
    else
        export PYTHONPATH="$ACCEPTANCE_TEST_ROOT_DIR:$PYTHONPATH"
    fi
}


verify_script_parameters $*

SCRIPT_FILE_DIR="`dirname $0`"
TESTING_SCRIPTS_DIR="`cd $SCRIPT_FILE_DIR; pwd`"
PROJECT_NAME="$1"
ACCEPTANCE_TEST_ROOT_DIR="`cd $TESTING_SCRIPTS_DIR/../../tests/$PROJECT_NAME/acceptance; pwd`"

RC_SERVER_LOG_PATH="$2"
XVFB_LOG_PATH=""

RC_SERVER_WAS_STARTED_BY_THIS_SCRIPT="Y"
XVFB_WAS_STARTED_BY_THIS_SCRIPT="Y"

if [ -e "$RC_SERVER_LOG_PATH/rc_server.pid" ]; then
    RC_SERVER_WAS_STARTED_BY_THIS_SCRIPT="N"
fi

if [ -n "$3" ]; then
    XVFB_LOG_PATH="$3"

    if [ -e "$XVFB_LOG_PATH/xvfb.pid" ]; then
        XVFB_WAS_STARTED_BY_THIS_SCRIPT="N"
    fi
fi

"$TESTING_SCRIPTS_DIR/ensure_selenium_rc_server_has_started.sh" "$RC_SERVER_LOG_PATH" "$XVFB_LOG_PATH"

# proceed if no error codes returned from last script
if [ $? -eq 0 ]; then
    set_python_path_for_acceptance_tests

    # use the Xvfb display if available
    if [ -n "$XVFB_LOG_PATH" -a -e "$XVFB_LOG_PATH/xvfb_display.txt" ]; then
        XVFB_DISPLAY="`cat $XVFB_LOG_PATH/xvfb_display.txt`"

        export DISPLAY=$XVFB_DISPLAY

        if [ "$RC_SERVER_WAS_STARTED_BY_THIS_SCRIPT" = "N" ]; then
            echo "Xvfb running on display $XVFB_DISPLAY"
            echo "Xvfb log path: $XVFB_LOG_PATH"
            echo "Selenium RC server log path: $RC_SERVER_LOG_PATH"
        fi

        echo "DISPLAY environment variable is $DISPLAY"
        printf "Running tests in headless mode on display $DISPLAY\n\n"
    fi

    "$ACCEPTANCE_TEST_ROOT_DIR/all_test_suites.py"

    if [ "$RC_SERVER_WAS_STARTED_BY_THIS_SCRIPT" = "Y" ]; then
        "$TESTING_SCRIPTS_DIR/stop_selenium_rc_server.py" "$RC_SERVER_LOG_PATH"

        if [ -n "$XVFB_LOG_PATH" -a "$XVFB_WAS_STARTED_BY_THIS_SCRIPT" = "Y" ]; then
            "$TESTING_SCRIPTS_DIR/stop_xvfb.py" "$XVFB_LOG_PATH"
        fi
    fi
else
    printf "\nUnable to start Selenium RC server or Xvfb due to errors above\n"
fi
