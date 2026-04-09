#!/bin/bash
# Project Machine — Install Script

SKILLS_DIR="$HOME/.claude/skills/project-machine"

echo "Installing Project Machine..."

mkdir -p "$SKILLS_DIR/agents"
cp CLAUDE.md "$SKILLS_DIR/"
cp presentation-spec.md "$SKILLS_DIR/"
cp agents/researcher.md "$SKILLS_DIR/agents/"
cp agents/analyst.md "$SKILLS_DIR/agents/"
cp agents/writer.md "$SKILLS_DIR/agents/"
cp agents/designer.md "$SKILLS_DIR/agents/"

echo ""
echo "Installed to: $SKILLS_DIR"
echo ""
echo "Usage:"
echo "  claude --dangerously-skip-permissions"
echo "  > Run project-machine on this brief: [your topic]"
