export function formatDate(date: Date): string {
    const months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ];

    const day = date.getDate();
    const monthIndex = date.getMonth();
    const year = date.getFullYear();

    return `${months[monthIndex]} ${day} ${year}`;
}

export function formatDateTime(date: Date): string {
    const weekdays = [
        "Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"
    ];

    const months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ];

    const day = weekdays[date.getDay()];
    const month = months[date.getMonth()];
    const dayOfMonth = date.getDate();
    const year = date.getFullYear();
    let hour = date.getHours();
    const minutes = date.getMinutes();
    let period = "AM";

    if (hour > 12) {
        hour -= 12;
        period = "PM";
    }

    return `${day}, ${month} ${dayOfMonth}, ${year} at ${hour}:${minutes.toString().padStart(2, "0")} ${period}`;
}

export function getAmountOfDays(date: Date): string {
    const oneDayMs = 24 * 60 * 60 * 1000; // number of milliseconds in a day
    const today = new Date();
    const diffDays = Math.round(Math.abs((today.getTime() - date.getTime()) / oneDayMs));
    if (diffDays === 0) {
        return "Today";
    } else if (diffDays === 1) {
        return "Yesterday";
    } else {
        return `${diffDays} days ago`;
    }
}