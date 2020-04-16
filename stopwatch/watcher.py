import time
import json
import os, sys, types

class Watcher(object):
    def __init__(self, td=False, upload_s3_path=None):
        self.points = {}
        self.time_debug = td
        self.s3_path = upload_s3_path

    def watch(self, target, arg_list=None, name=None):
        timer_start = time.time()
        if isinstance(arg_list, list):
            res = target(*arg_list)
        else:
            res = target
        break_time = time.time()
        consumed = break_time - timer_start

        last_key = len(self.points.keys())
        to_add_index_n = last_key
        self.points[to_add_index_n] = consumed
        if self.time_debug:
            if name != None:
                print("[BreakTime] {} consumed time : {}".format(name, consumed))
            else:
                print("[BreakTime] {} consumed time : {}".format(to_add_index_n, consumed))

        return [res, consumed]
