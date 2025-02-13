"""Send greetings."""

import arrow

def greet(tz):
    """Greet a location."""
    now = arrow.now(tz)
    friendly_time = now.format("h:mm a")
    location = tz.split("/")[-1].replace("_"," ") 
    return f"Hello, {location}! The time is {friendly_time}."
# Ensure this runs when the module is executed directly
if __name__ == "__main__":
    # Check if a timezone argument was provided
    if len(sys.argv) > 1:
        timezone = sys.argv[1]
    else:
        timezone = "UTC"  # Default to UTC if no argument is given

    print(greet(timezone))
