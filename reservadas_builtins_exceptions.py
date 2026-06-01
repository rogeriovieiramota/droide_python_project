import keyword
import builtins

# === KEYWORDS ===
print("=== KEYWORDS ===")
for i, kw in enumerate(keyword.kwlist, start=1):
    print(f"{i}, {kw}")

# === BUILT-IN FUNCTIONS ===
print("\n=== BUILT-IN FUNCTIONS ===")
for i, func in enumerate(dir(__builtins__), start=1):
    print(f"{i}, {func}")

# === BUILT-IN EXCEPTIONS ===
print("\n=== BUILT-IN EXCEPTIONS ===")
exceptions = [name for name in dir(builtins) if name.endswith("Error")]
for i, exc in enumerate(exceptions, start=1):
    print(f"{i}, {exc}")
