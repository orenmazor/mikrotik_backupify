# Usage

> uv run backup.py

The purpose of this script is to run in my homelab and backup my router configuration daily to a local folder.

The output is to a folder called `/output/`, which is a mounted path.

This path is monitored by Restic, which is how my backup works.

There are many backup strategies. This one's mine.
