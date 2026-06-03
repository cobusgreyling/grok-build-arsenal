#!/usr/bin/env bash
#
# Grok Build Arsenal — One-command skill & template installer
#
# Usage:
#   bash scripts/install-skills.sh                  # install into current project .grok/skills
#   bash scripts/install-skills.sh --global         # install into ~/.grok/skills (user level)
#   bash scripts/install-skills.sh --target /path   # install into specific project
#
# This makes the "copy skills" story in the README actually frictionless.
#
# Sole author: Cobus Greyling

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_SRC="$REPO_ROOT/skills"
TEMPLATES_SRC="$REPO_ROOT/templates"
MCP_SRC="$REPO_ROOT/mcps"

TARGET=""
GLOBAL=false
DRY_RUN=false

print_help() {
  cat <<EOF
Grok Build Arsenal Installer

Options:
  --global          Install skills to ~/.grok/skills (user-wide)
  --target <path>   Install into a specific project root (will create .grok/skills)
  --dry-run         Show what would be done without making changes
  -h, --help        This help

Examples:
  cd my-project && bash /path/to/grok-build-arsenal/scripts/install-skills.sh
  bash scripts/install-skills.sh --global
  bash scripts/install-skills.sh --target ~/projects/foo
EOF
}

while [[ $# -gt 0 ]]; do
  case $1 in
    --global)
      GLOBAL=true
      shift
      ;;
    --target)
      TARGET="$2"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    -h|--help)
      print_help
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      print_help
      exit 1
      ;;
  esac
done

if $GLOBAL; then
  TARGET_DIR="${HOME}/.grok/skills"
elif [[ -n "$TARGET" ]]; then
  TARGET_DIR="$TARGET/.grok/skills"
else
  # default: current directory as project
  TARGET_DIR="$(pwd)/.grok/skills"
fi

echo "Grok Build Arsenal — Skill Installer"
echo "Source: $SKILLS_SRC"
echo "Target: $TARGET_DIR"
echo

if $DRY_RUN; then
  echo "[DRY RUN] Would create $TARGET_DIR and copy skills..."
  for d in "$SKILLS_SRC"/*/; do
    [[ -d "$d" ]] && echo "  - $(basename "$d")"
  done
  exit 0
fi

mkdir -p "$TARGET_DIR"

copied=0
for skill_dir in "$SKILLS_SRC"/*/; do
  if [[ -d "$skill_dir" ]]; then
    skill_name=$(basename "$skill_dir")
    dest="$TARGET_DIR/$skill_name"
    if [[ -d "$dest" ]]; then
      echo "  ~ Updating $skill_name"
      rm -rf "$dest"
    else
      echo "  + Installing $skill_name"
    fi
    # Copy the skill directory (not just contents) — use dest explicitly
    cp -R "$skill_dir" "$dest"
    ((copied++))
  fi
done

echo
echo "Installed/updated $copied skills into $TARGET_DIR"

# Also offer to copy a template's .grok bits if user wants a full starter
if [[ -z "$TARGET" ]] && ! $GLOBAL; then
  echo
  echo "Tip: For a full project starter (AGENTS.md + .grok config + hooks), copy one of:"
  echo "  cp -R $TEMPLATES_SRC/python-fastapi-grok/. /path/to/new-project/"
  echo "  cp -R $TEMPLATES_SRC/nextjs-grok/. /path/to/new-project/"
  echo "  cp -R $TEMPLATES_SRC/rust-cli-grok/. /path/to/new-project/"
fi

echo
echo "Next steps:"
echo "  grok inspect          # verify the new skills are discovered"
echo "  grok                  # start a session and try 'use plan-mode-orchestrator'"
echo
echo "Done. All original work by Cobus Greyling."