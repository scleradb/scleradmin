import sys
import os
import argparse

from . import install

def main():
    """Parse arguments and call the installer"""

    parser = argparse.ArgumentParser(
        description = "Sclera Platform Administration",
        epilog = "In --add and --remove above, 'package' has the format 'org:name:version', where 'org:' and ':version' are optional. When not specified, 'org' defaults to 'com.scleradb' and 'version' defaults to the latest integration version. Sclera requires Java version 8 or higher."
    )

    parser.add_argument(
        "--install", action = "store_true",
        help = "install Sclera in the home directory"
    )

    parser.add_argument(
        "--add", metavar = "package", type = str, nargs = "+",
        help = "add packages"
    )

    parser.add_argument(
        "--remove", metavar = "package", type = str, nargs = "+",
        help = "remove packages"
    )

    parser.add_argument(
        "--update", action = "store_true",
        help = "update the installed packages to the latest version"
    )

    parser.add_argument(
        "--home", metavar = "homedir", type = str, nargs = 1,
        default = [os.getenv("SCLERA_HOME", os.path.expanduser("~/sclera"))],
        help = "home directory location (if not specified, will use $SCLERA_HOME if present, otherwise ~/sclera)"
    )

    parser.add_argument(
        "--overwrite", action = "store_true",
        help = "overwrite home directory if present"
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    try:
        install.run(args)
    except ConnectionError:
        sys.exit("Could not connect to the internet. Exiting.")
    except Exception as e:
        sys.exit(e)
