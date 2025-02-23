#!/usr/bin/env bash
# Use this script to test if a given TCP host/port are available

TIMEOUT=15
QUIET=0
HOST=""
PORT=""

echoerr() { if [[ $QUIET -ne 1 ]]; then echo "$@" 1>&2; fi }

usage()
{
    exit 1
}

wait_for()
{
    for i in `seq $TIMEOUT` ; do
        nc -z "$HOST" "$PORT" > /dev/null 2>&1
        result=$?
        if [[ $result -eq 0 ]] ; then
            return 0
        fi
        sleep 1
    done
    echo "Operation timed out" >&2
    return 1
}

while [[ $# -gt 0 ]]
do
    case "$1" in
        --timeout=*)
        TIMEOUT="${1#*=}"
        shift 1
        ;;
        --quiet)
        QUIET=1
        shift 1
        ;;
        --)
        shift
        break
        ;;
        *)
        break
        ;;
    esac
done

HOST=$1
PORT=$2

if [[ "$HOST" == "" || "$PORT" == "" ]]; then
    usage
fi

wait_for
result=$?

exit $result
