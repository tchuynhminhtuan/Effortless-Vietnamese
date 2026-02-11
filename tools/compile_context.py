import os

# Configuration
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "EFFORTLESS_VIETNAMESE_FULL_CONTEXT.md")

# Directories to include (Relative to Project Root)
INCLUDE_DIRS = [
    "foundation",
    "content",
    "marketing",
    "production",
    "compliance",
    "tools/engagement_app" # Include the source code of the app as it's critical
]

# Files to include explicitly
INCLUDE_FILES = [
    "README.md",
    "DOCUMENTATION_MAP.md"
]

# Extensions to look for
VALID_EXTENSIONS = {".md", ".html", ".css", ".js", ".py"}

def compile_context():
    print(f"🚀 Starting context compilation...")
    print(f"📂 Project Root: {PROJECT_ROOT}")
    
    content_buffer = []

    # Header
    content_buffer.append(f"# EFFORTLESS VIETNAMESE - PREPARED CONTEXT FOR AI AGENTS\n")
    content_buffer.append(f"> This document contains the full project documentation and source code for the Effortless Vietnamese project.\n")
    content_buffer.append(f"> Auto-generated for use in Gemini / NotebookML.\n\n")

    # Process explicit files
    for filename in INCLUDE_FILES:
        filepath = os.path.join(PROJECT_ROOT, filename)
        if os.path.exists(filepath):
            append_file(filepath, content_buffer)

    # Process directories
    for dirname in INCLUDE_DIRS:
        dirpath = os.path.join(PROJECT_ROOT, dirname)
        if not os.path.exists(dirpath):
            print(f"⚠️ Directory not found: {dirname}")
            continue
            
        for root, _, files in os.walk(dirpath):
            for file in files:
                if any(file.endswith(ext) for ext in VALID_EXTENSIONS):
                    filepath = os.path.join(root, file)
                    # Skip the output file itself if it ends up in the path
                    if os.path.abspath(filepath) == os.path.abspath(OUTPUT_FILE):
                        continue
                    append_file(filepath, content_buffer)

    # Write output
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(content_buffer))
    
    print(f"✅ Comparison complete! Output saved to:\n👉 {OUTPUT_FILE}")

def append_file(filepath, buffer):
    rel_path = os.path.relpath(filepath, PROJECT_ROOT)
    print(f"   📄 Adding: {rel_path}")
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            file_content = f.read()
            
        buffer.append(f"\n{'='*50}")
        buffer.append(f"FILE PATH: {rel_path}")
        buffer.append(f"{'='*50}\n")
        
        ext = os.path.splitext(filepath)[1][1:] # get extension without dot
        if ext == "md":
            buffer.append(file_content)
        elif ext in ["html", "js", "py", "css"]:
            buffer.append(f"```{ext}")
            buffer.append(file_content)
            buffer.append(f"```")
        else:
            buffer.append(file_content)
            
        buffer.append("\n") # Formatting spacer
    except Exception as e:
        print(f"❌ Error reading {rel_path}: {e}")

if __name__ == "__main__":
    compile_context()
