$(document).ready(function () {
    $(".filter-topic").on("change", function () {
        const topicId = $(this).val();
        $.ajax({
            url: "/newspapers/",
            type: "GET",
            data: { topic: topicId },
            success: function (response) {
                $(".newspaper-list").html(response);
            },
            error: function (xhr, status, error) {
                console.error("Error loading newspapers:", error);
            }
        });
    });
});
