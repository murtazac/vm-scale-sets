'''get_vmss_rolling_upgrade.py - get details about rolling upgrades for a VM scale set'''
import argparse
import json
import sys

import azurerm


def main():
    '''Main routine.'''
    # validate command line arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--vmssname', '-n', required=True, action='store', help='VMSS Name')
    arg_parser.add_argument('--rgname', '-g', required=True, action='store',
                            help='Resource Group Name')
    arg_parser.add_argument('--details', '-a', required=False, action='store_true',
                            default=False, help='Print all details')
    args = arg_parser.parse_args()

    name = args.vmssname
    rgname = args.rgname
    details = args.details

    # authenticate
    access_token = azurerm.get_access_token_from_cli()
    subscription_id = azurerm.get_subscription_from_cli()

    # get rolling upgrade latest status
    upgrade_status = azurerm.get_vmss_rolling_upgrades(
        access_token, subscription_id, rgname, name)

    # print details
    if details is True:
        print(json.dumps(upgrade_status, sort_keys=False,
                         indent=2, separators=(',', ': ')))
    else:
        print(json.dumps(upgrade_status, sort_keys=False,
                         indent=2, separators=(',', ': ')))


if __name__ == "__main__":
    main()
