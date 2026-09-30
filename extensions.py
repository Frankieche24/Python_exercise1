"""File extensions: prompt for a file name and print its media type."""

from pathlib import PurePath

# Extension (lowercase, with leading dot) -> media type
MEDIA_TYPES = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip",
}

DEFAULT_TYPE = "application/octet-stream"


def main():
    filename = input("File name: ")
    print(media_type(filename))


def media_type(filename):
    """Return the media type for a file name, ignoring case and outer spaces.

    Only the LAST extension counts ("a.tar.gz" -> ".gz").
    Unknown, missing, or empty extensions give the default binary type.
    """
    extension = PurePath(filename.strip()).suffix.lower()
    return MEDIA_TYPES.get(extension, DEFAULT_TYPE)


if __name__ == "__main__":
    main()
