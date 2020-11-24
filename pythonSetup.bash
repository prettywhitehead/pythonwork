#! /bin/bash

function usage () { echo "BASIC USAGE: pythonSetup.bash -v|--version"
                    echo "Example: pythonSetup.bash using default version ||  pythonSetup.bash -v 2.7.10"
                  }

v=2.7
skip=0
curDir=`pwd`
export PYTHON_PKG=/Users/josephwu/Downloads/PYTHON_PKG
export PYTHONPATH=$PYTHONPATH:/Users/josephwu/pythonWorkSpace/myPkg
while [[ $# -gt 0 ]]
do
        case $1 in
                -v|version) shift
                v=$1
                ;;
                -h|help)
                skip=1
                usage
                break
                ;;
                *)
                skip=1
                usage
                break
                ;;
        esac
        shift
done

if [[ $skip -eq 0 ]] 
then
printf "Building Python Virtual ENV with python version $v ...\n"

#virtualenv -p  /usr/bin/python$v  --system-site-packages $curDir/virtualenv
virtualenv -p  /usr/local/bin/python$v  --system-site-packages $curDir/virtualenv
. $curDir/virtualenv/bin/activate
pip install --no-index --find-links=$PYTHON_PKG \
            -r "reqPackage.txt"
fi
