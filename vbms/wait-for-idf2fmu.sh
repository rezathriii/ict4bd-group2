#!/bin/bash

echo "Waiting 30 seconds before starting VBMS..."
sleep 30

echo "Starting VBMS..."
exec python app.py
