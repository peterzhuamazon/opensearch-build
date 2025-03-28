#!/bin/bash

# Copyright OpenSearch Contributors
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

set -ex

function usage() {
    echo "Usage: $0 [args]"
    echo ""
    echo "Arguments:"
    echo -e "-v VERSION\t[Required] OpenSearch version."
    echo -e "-s SNAPSHOT\t[Optional] Build a snapshot, default is 'false'."
    echo -e "-p PLATFORM\t[Optional] Platform, default is 'uname -s'."
    echo -e "-a ARCHITECTURE\t[Optional] Build architecture, default is 'uname -m'."
    echo -e "-f ARTIFACTS\t[Optional] Location of build artifacts."
    echo -e "-o OUTPUT\t[Optional] Output path."
    echo -e "-h help"
}

while getopts ":h:v:s:o:p:a:f:" arg; do
    case $arg in
        h)
            usage
            exit 1
            ;;
        v)
            VERSION=$OPTARG
            ;;
        s)
            SNAPSHOT=$OPTARG
            ;;
        o)
            OUTPUT=$OPTARG
            ;;
        p)
            PLATFORM=$OPTARG
            ;;
        a)
            ARCHITECTURE=$OPTARG
            ;;
        f)
            ARTIFACTS=$OPTARG
            ;;
        :)
            echo "Error: -${OPTARG} requires an argument"
            usage
            exit 1
            ;;
        ?)
            echo "Invalid option: -${arg}"
            exit 1
            ;;
    esac
done

if [ -z "$VERSION" ]; then
    echo "Error: missing version."
    usage
    exit 1
fi

[ -z "$SNAPSHOT" ] && SNAPSHOT="false"
[ -z "$PLATFORM" ] && PLATFORM=$(uname -s | awk '{print tolower($0)}')
[ -z "$ARCHITECTURE" ] && ARCHITECTURE=`uname -m`

## Setup Performance Analyzer Agent
# mv $OUTPUT/plugins/opensearch-performance-analyzer/performance-analyzer-rca $OUTPUT/

## Performance Analyzer Configs
if echo $ARTIFACTS | grep -Eo '/deb/|/rpm/'; then
    echo "DEB/RPM configs"
    #echo 'true' > $OUTPUT/../var/lib/opensearch/rca_enabled.conf
    echo 'true' > $OUTPUT/../var/lib/opensearch/performance_analyzer_enabled.conf
fi
