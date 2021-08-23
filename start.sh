#!/bin/bash
tmux new -d -s reactbot
tmux send -t reactbot "python3 react.py" ENTER
echo "Tmux session started. Use \"tmux a -t reactbot\" to attach to the session"