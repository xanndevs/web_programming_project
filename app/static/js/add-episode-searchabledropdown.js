$(document).ready(function () {
    // Show the dropdown when the search input is focused
    $('#search').on('focus', function () {
        $('#dropdown').show();
    });

    // Hide the dropdown when clicking outside the input and dropdown
    $(document).on('mousedown', function (event) {
        if (!$(event.target).closest('.dropdown-searchable').length) {
            $('#dropdown').hide();
        }
    });

    // Filter options based on search input
    $('#search').on('keyup', function () {
        var searchText = $(this).val().toLowerCase();
        $('#dropdown option').each(function () {
            var optionText = $(this).text().toLowerCase();
            if (optionText.indexOf(searchText) > -1) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });

    // Optional: Hide the dropdown when an option is clicked

    $('#dropdown').on('change', function () {
        elem = document.getElementById("dropdown");
        $('#search').attr('value',elem.options[elem.selectedIndex].text);
        $('#dropdown').hide();
    });
});