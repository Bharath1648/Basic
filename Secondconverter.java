public static String convertSeconds(int seconds) {
    int hours = seconds / 3600;
    int minutes = (seconds % 3600) / 60;
    int remainingSeconds = seconds % 60;

    // Formatting the result as a string
    String result = String.format("%02d:%02d:%02d", hours, minutes, remainingSeconds);

    return result;
}
