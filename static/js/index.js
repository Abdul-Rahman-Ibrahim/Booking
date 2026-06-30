document.addEventListener("DOMContentLoaded", () => {

    const calendarEl = document.getElementById("calendar");
    const equipmentCheckboxes = document.querySelectorAll(".equipment-list input[type='checkbox']");

    function getVisibleBookings() {
        const checkedEquipmentIds = new Set(
            Array.from(equipmentCheckboxes)
                .filter((checkbox) => checkbox.checked)
                .map((checkbox) => String(checkbox.value))
        );

        return BOOKINGS.filter((booking) => {
            const equipmentId = booking?.extendedProps?.equipmentId;
            return checkedEquipmentIds.has(String(equipmentId));
        });
    }

    const calendar = new FullCalendar.Calendar(calendarEl, {

        initialView: "timeGridThreeDay",

        headerToolbar: false,

        selectable: true,

        editable: true,

        slotEventOverlap: false,

        eventMaxStack: 10,


        nowIndicator: true,

        allDaySlot: false,

        slotDuration: "01:00:00",

        slotLabelInterval: "01:00",

        slotMinTime: "00:00:00",

        slotMaxTime: "24:00:00",

        expandRows: false,

        stickyHeaderDates: true,

        height: "100%",

        events: getVisibleBookings(),

        slotLabelFormat: {
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        },

        eventTimeFormat: {
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        },

        views: {

            timeGridThreeDay: {

                type: "timeGrid",

                duration: { days: 3 }

            }

        }

    });

    calendar.render();

    function refreshVisibleBookings() {
        calendar.removeAllEventSources();
        calendar.addEventSource(getVisibleBookings());
    }

    equipmentCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener("change", refreshVisibleBookings);
    });

    calendar.scrollToTime('08:00:00');

    //--------------------------------------------------
    // Update title
    //--------------------------------------------------

    function updateTitle() {

        document.getElementById("calendar-title").textContent =
            calendar.view.title;

    }

    updateTitle();

    calendar.on("datesSet", updateTitle);

    //--------------------------------------------------
    // Navigation
    //--------------------------------------------------

    document
        .getElementById("fc-prev")
        .addEventListener("click", () => {

            calendar.prev();

        });

    document
        .getElementById("fc-next")
        .addEventListener("click", () => {

            calendar.next();

        });

    document
        .getElementById("fc-today")
        .addEventListener("click", () => {

            calendar.today();

        });

    //--------------------------------------------------
    // View buttons
    //--------------------------------------------------

    const buttons = document.querySelectorAll(".view-tab");

    function activate(btn) {

        buttons.forEach(b => b.classList.remove("active"));

        btn.classList.add("active");

    }

    document
        .getElementById("view-day")
        .onclick = function () {

            activate(this);

            calendar.changeView("timeGridDay");

        };

    document
        .getElementById("view-3day")
        .onclick = function () {

            activate(this);

            calendar.changeView("timeGridThreeDay");

        };

    document
        .getElementById("view-week")
        .onclick = function () {

            activate(this);

            calendar.changeView("timeGridWeek");

        };

    document
        .getElementById("view-month")
        .onclick = function () {

            activate(this);

            calendar.changeView("dayGridMonth");

        };

});
