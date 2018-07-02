#!/bin/sh
DIR=`dirname $0`
VERBE=`shuf -n 1 $DIR/verbes.txt`
NOM=`shuf -n 1 $DIR/noms.txt`
echo $VERBE $NOM...

