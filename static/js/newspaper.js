$(document).ready(function () {
    // Фільтрація за темами
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

    // Пошук газет
    $("#search-input").on("keyup", function () {
        const query = $(this).val();
        $.ajax({
            url: "/newspapers/search/",
            type: "GET",
            data: { q: query },
            success: function (response) {
                $(".newspaper-list").html(response);
            },
            error: function (xhr, status, error) {
                console.error("Error searching newspapers:", error);
            }
        });
    });

    // Сортування газет
    $(".sort-newspapers").on("change", function () {
        const sortOption = $(this).val();
        $.ajax({
            url: "/newspapers/",
            type: "GET",
            data: { sort: sortOption },
            success: function (response) {
                $(".newspaper-list").html(response);
            },
            error: function (xhr, status, error) {
                console.error("Error sorting newspapers:", error);
            }
        });
    });

    // Завантаження додаткових газет (пагінація)
    $(".load-more").on("click", function () {
        const page = $(this).data("page");
        $.ajax({
            url: "/newspapers/",
            type: "GET",
            data: { page: page },
            success: function (response) {
                $(".newspaper-list").append(response);
                $(".load-more").data("page", page + 1);
            },
            error: function (xhr, status, error) {
                console.error("Error loading more newspapers:", error);
            }
        });
    });

    // Динамічне завантаження деталей газети
    $(".newspaper-item a").on("click", function (e) {
        e.preventDefault();
        const detailUrl = $(this).attr("href");
        $.ajax({
            url: detailUrl,
            type: "GET",
            success: function (response) {
                $(".modal-content").html(response);
                $(".modal").fadeIn();
            },
            error: function (xhr, status, error) {
                console.error("Error loading newspaper details:", error);
            }
        });
    });

    // Закриття модального вікна
    $(".modal-close").on("click", function () {
        $(".modal").fadeOut();
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const newsContainer = document.getElementById('latest-news');

    fetch('/api/latest-news/')
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                data.forEach(news => {
                    const newsItem = document.createElement('div');
                    newsItem.className = 'news-item';
                    newsItem.innerHTML = `
                        <h4><a href="/newspaper/${news.id}/">${news.title}</a></h4>
                        <p>Published on: ${news.published_date}</p>
                    `;
                    newsContainer.appendChild(newsItem);
                });
            } else {
                newsContainer.innerHTML = '<p>No latest news available.</p>';
            }
        })
        .catch(error => {
            console.error('Error fetching latest news:', error);
            newsContainer.innerHTML = '<p>Error loading latest news.</p>';
        });
});
