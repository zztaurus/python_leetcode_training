
def compareVersion(version1: str, version2: str) -> int:
    # Split the version strings into parts
    v1_parts = version1.split('.')
    v2_parts = version2.split('.')

    # Determine the maximum length of the two version parts
    max_length = max(len(v1_parts), len(v2_parts))

    # Compare each part of the version numbers
    for i in range(max_length):
        # Convert the current part to an integer, defaulting to 0 if the part is missing
        v1_part = int(v1_parts[i]) if i < len(v1_parts) else 0
        v2_part = int(v2_parts[i]) if i < len(v2_parts) else 0

        # Compare the current parts
        if v1_part > v2_part:
            return 1
        elif v1_part < v2_part:
            return -1

    # If all parts are equal, return 0
    return 0





if __name__ == '__main__':
    # version1 = "1.1"
    # version2 = "1.001"
    # compareVersion(version1, version2)

    # Example usage:
    print(compareVersion("1.01", "1.001"))  # Output: 0
    print(compareVersion("1.0", "1.0.0"))  # Output: 0
    print(compareVersion("0.1", "1.1"))
    print(compareVersion("1.2", "1.10")) 




