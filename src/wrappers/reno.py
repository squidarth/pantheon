#!/usr/bin/env python

from subprocess import check_call

import arg_parser
import context
from helpers import kernel_ctl


def setup_reno():
    return
    # check if qdisc is fq_codel
    #kernel_ctl.check_qdisc('fq_codel')


def main():
    args = arg_parser.receiver_first()

    if args.option == 'deps':
        print 'iperf'
        return

    if args.option == 'setup_after_reboot':
        setup_reno()
        return

    if args.option == 'receiver':
        cmd = ['iperf', '-Z', 'reno', '-s', '-p', args.port]
        check_call(cmd)
        return

    if args.option == 'sender':
        cmd = ['iperf', '-Z', 'reno', '-c', args.ip, '-p', args.port,
               '-t', '75']
        check_call(cmd)
        return


if __name__ == '__main__':
    main()
