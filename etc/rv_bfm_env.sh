#!/bin/sh

etc_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd)"
RV_BFMS=`cd $etc_dir/.. ; pwd`
export RV_BFMS

# Add a path to the simscripts directory
export PATH=$RV_BFMS/packages/simscripts/bin:$PATH

# Force the PACKAGES_DIR
export PACKAGES_DIR=$RV_BFMS/packages

