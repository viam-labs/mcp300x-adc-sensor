#!/usr/bin/env bash

set -euo pipefail

cd $(dirname $0)

# Create a virtual environment to run our code
VENV_NAME="venv"
PYTHON="$VENV_NAME/bin/python"
ENV_ERROR="This module requires Python >=3.8, pip, and virtualenv to be installed."

export PATH=$PATH:$HOME/.local/bin

if [ ! "$(command -v uv)" ]; then
  if [ ! "$(command -v curl)" ]; then
    echo "curl is required to install UV. please install curl on this system to continue."
    exit 1
  fi
  echo "Installing uv command"
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi

uv venv $VENV_NAME

uv pip sync requirements.txt