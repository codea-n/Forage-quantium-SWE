#!/bin/bash

#activate virtual environment
source ./.venv/Scripts/activate

if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual environment is activated: $VIRTUAL_ENV"
else
    echo "Virtual environment is NOT activated"
fi


# Run tests using pytest
pytest

if [ $? -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
