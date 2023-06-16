def convert_timestamp(timestamp: str, format = "%Y-%m-%dT%H:%M:%SZ") -> str:
    """Converts a timestamp string in ISO 8601 format to a simpler format without microseconds."""
    
    # Remove the single quotes from the timestamp
    timestamp = timestamp.strip("'")

    # Split the timestamp into the scorecard_notification_main part and the microseconds part
    main, _, _ = timestamp.partition(".")

    try:
        dt = datetime.strptime(main, "%Y-%m-%dT%H:%M:%S")
        return dt.strftime(format)
    except ValueError:
        log.error(f"Unrecognized timestamp format: {timestamp} from {main}")
        return timestamp #f"'{timestamp}'"  # return original if format not recognized
