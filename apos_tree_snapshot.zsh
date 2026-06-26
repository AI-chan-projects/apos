#!/bin/zsh

# ------------------------------------
# APOS TREE SNAPSHOT TOOL
# ------------------------------------
# Usage:
#   chmod +x apos_tree_snapshot.zsh
#   ./apos_tree_snapshot.zsh
# ------------------------------------

TARGET_DIR=${1:-scripts}
OUTPUT_FILE=${2:-apos_tree_snapshot.txt}

echo "🌳 APOS Tree Snapshot Generator"
echo "Target: $TARGET_DIR"
echo "Output: $OUTPUT_FILE"
echo "------------------------------------"

# check if directory exists
if [ ! -d "$TARGET_DIR" ]; then
  echo "❌ Directory not found: $TARGET_DIR"
  exit 1
fi

# generate tree (limit depth for readability)
if command -v tree >/dev/null 2>&1; then
  tree -L 6 "$TARGET_DIR" > "$OUTPUT_FILE"
else
  echo "⚠️ 'tree' not found. Using fallback 'find'..."

  echo "$TARGET_DIR" > "$OUTPUT_FILE"
  find "$TARGET_DIR" -maxdepth 6 | sed 's|[^/]*/|  |g' >> "$OUTPUT_FILE"
fi

echo "✅ Snapshot saved to: $OUTPUT_FILE"

# optional: print preview
echo ""
echo "📌 Preview:"
echo "------------------------------------"
head -n 60 "$OUTPUT_FILE"
echo "------------------------------------"