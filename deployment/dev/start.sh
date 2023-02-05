#!/bin/bash

echo "Migrating..."
make migrate
echo "Collecting static..."
make collectstatic
echo "Starting application..."
make run
