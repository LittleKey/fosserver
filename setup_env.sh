#!/usr/bin/env sh

ENV_PATH=${HOME}/.Envs
SOURCE_NAME="fosserver"
SOURCE_PATH="${ENV_PATH}/${SOURCE_NAME}"
PYTHON_PATH="$(which python3)"
SCRIPT_PATH="${HOME}/.zshrc"
DEPENDENCYS=("tornado" "six" "redis" "pony")

if [ ! -d ${ENV_PATH} ];
then
    mkdir -p ${ENV_PATH}
    echo 'export WORKON_HOME='${ENV_PATH} >> ${SCRIPT_PATH}
    echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ${SCRIPT_PATH}
    echo 'alias workoff=deactivate' >> ${SCRIPT_PATH}
fi
export WORKON_HOME=${ENV_PATH}
source /usr/local/bin/virtualenvwrapper.sh
if [ ! -d ${SOURCE_PATH} ];
then
    mkvirtualenv -p ${PYTHON_PATH} ${SOURCE_NAME}
else
    workon ${SOURCE_NAME}
fi
for package in "${DEPENDENCYS[@]}"
do
    if [ ! -n "$(lssitepackages | grep ${package})" ];
    then
        pip install ${package}
    fi
done
