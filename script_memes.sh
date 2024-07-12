#!/bin/bash

uvicorn app.memes.main:memes_app --host 0.0.0.0 --port 8000
