import shutil
import logging
from pathlib import Path
from datetime import datetime

SOURCE = Path(r"C:\path\to\source")        # predesignated source
DEST   = Path(r"C:\path\to\destination")   # predesignated target
PATTERN = "*.csv"                          # which files; use "*" for everything

logging.basicConfig(
    filename="file_mover.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

def move_files(source: Path, dest: Path, pattern: str = "*") -> int:
    if not source.is_dir():                     # guard: source must exist
        logging.error("Source folder missing: %s", source)
        return 0
    dest.mkdir(parents=True, exist_ok=True)     # create target if absent

    moved = 0
    for item in source.glob(pattern):
        if not item.is_file():                  # skip subfolders
            continue
        target = dest / item.name
        if target.exists():                     # avoid silent overwrite
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            target = dest / f"{item.stem}_{stamp}{item.suffix}"
        try:
            shutil.move(str(item), str(target))
            logging.info("Moved %s -> %s", item.name, target)
            moved += 1
        except (OSError, shutil.Error) as e:
            logging.error("Failed to move %s: %s", item.name, e)

    logging.info("Done. %d file(s) moved.", moved)
    return moved

if __name__ == "__main__":
    move_files(SOURCE, DEST, PATTERN)
