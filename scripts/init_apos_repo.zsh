#!/usr/bin/env zsh

PROJECT_NAME="apos-runtime"

echo "Creating APOS Minimal Runtime Repository: $PROJECT_NAME"

mkdir -p $PROJECT_NAME
cd $PROJECT_NAME

# Core layers
mkdir -p core/air
mkdir -p core/policy
mkdir -p core/kernel
mkdir -p core/event_store
mkdir -p core/control_plane

# Runtime layer
mkdir -p runtime/executor
mkdir -p runtime/scheduler

# Interfaces
mkdir -p control_plane/telegram
mkdir -p control_plane/cli

# Observability
mkdir -p observability/metrics
mkdir -p observability/trace

# Memory (minimal placeholder for MVP)
mkdir -p memory/working
mkdir -p memory/project

# Data storage
mkdir -p data/events
mkdir -p data/snapshots

# Config
mkdir -p config

# Docs
mkdir -p docs

# Create minimal entry points

touch core/kernel/loop.py
touch core/event_store/store.py
touch core/policy/evaluator.py
touch core/air/generator.py

touch control_plane/telegram/bot.py
touch control_plane/cli/cli.py

touch runtime/executor/executor.py
touch runtime/scheduler/scheduler.py

touch observability/metrics/metrics.py
touch observability/trace/tracer.py

touch config/system.json

# Root entry point
touch main.py

# Basic README
cat <<EOF > README.md
# APOS Minimal Runtime

This is the minimal executable prototype of APOS.

Core Loop:
Human → AIR → Policy → Kernel → Event Store → Human
EOF

echo "APOS runtime structure created successfully."