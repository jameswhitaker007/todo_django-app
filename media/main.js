function getCookie(name) {
    let cookieValue = null; if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';'); for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) { cookieValue = decodeURIComponent(cookie.substring(name.length + 1)); break; }
        }
    } return cookieValue;
} const csrftoken = getCookie('csrftoken');

document.addEventListener("DOMContentLoaded", function () {
    const completedButtons = document.querySelectorAll(".completed-btn");
    if (completedButtons.length > 0) {
        completedButtons.forEach((button) => {
            button.addEventListener("click", function () {
                const todoId = button.getAttribute("data-id");
                fetch(`/todo/complete/${todoId}`, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": csrftoken,
                    },
                })
                    .then((response) => {
                        if (!response.ok) {
                            throw new Error("Network response was not ok");
                        }
                        return response.json();
                    })
                    .then((data) => {
                        console.log("Completed response");
                        window.location.reload();
                    })
                    .catch((error) => console.error);
            });
        });
    }
});