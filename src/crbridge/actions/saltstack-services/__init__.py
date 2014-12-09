#!/usr/bin/python
######################################################################
# Cloud Routes Bridge
# -------------------------------------------------------------------
# Actions Module
######################################################################

import syslog
import requests
import time


def false(redata, jdata, rdb, r_server):
    ''' This method will be called when a monitor has false '''
    run = True
    # Check for Trigger
    if redata['trigger'] > jdata['failcount']:
        run = False

    # Check for lastrun
    checktime = time.time() - float(redata['lastrun'])
    if checktime < redata['frequency']:
        run = False

    if redata['data']['call_on'] == 'true':
        run = False

    if run:
        return callSalt(redata, jdata)
    else:
        return None


def true(redata, jdata, rdb, r_server):
    ''' This method will be called when a monitor has passed '''
    run = True
    # Check for Trigger
    if redata['trigger'] > jdata['failcount']:
        run = False

    # Check for lastrun
    checktime = time.time() - float(redata['lastrun'])
    if checktime < redata['frequency']:
        run = False

    if redata['data']['call_on'] == 'false':
        run = False

    if run:
        return callSalt(redata, jdata)
    else:
        return None


def callSalt(redata, jdata):
    ''' Perform actual call '''
    url = redata['data']['url']
    payload = redata['data']
    try:
        req = requests.post(url, data=payload, timeout=3.00, verify=False)
    except:
        return False
    if req.status_code == 200:
        line = "saltstack-services: Reqeust to %s sent for monitor %s - Successful" % (url, jdata['cid'])
        syslog.syslog(syslog.LOG_INFO, line)
        return True
    else:
        line = "saltstack-services: Request to %s sent for monitor %s - False" % (url, jdata['cid'])
        syslog.syslog(syslog.LOG_INFO, line)
        return False
