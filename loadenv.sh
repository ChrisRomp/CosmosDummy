#!/bin/bash
# Loads environment from .env file
if [ ! -f .env ]
then
  export $(cat .env | xargs)
fi
