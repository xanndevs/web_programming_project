$(document).ready(function () {
    $('#search-add').on('focus', function () {
        $('#dropdown-add').show();
    });

    // Hide the dropdown when clicking outside the input and dropdown
    $(document).on('mousedown', function (event) {
        if (!$(event.target).closest('.dropdown-searchable-add').length) {
            $('#dropdown-add').hide();
        }
    });

    // Filter options based on search input
    $('#search-add').on('keyup', function () {
        var counter=0;
        var searchText = $(this).val().toLowerCase();
        $('#dropdown-add option').each(function () {
            var optionText = $(this).text().toLowerCase();
            if (optionText.indexOf(searchText) > -1) {
                $(this).show();
                counter++;
            } else {
                if(!$(this).is(":disabled"))$(this).hide();
            }
        });
        if(counter <= 1)counter = 2;
        if(counter > 10)counter = 10;
        $('#dropdown-add').attr('size', counter);
    });

    // Optional: Hide the dropdown when an option is clicked

    $('#dropdown-add').on('change', function () {
        elem = document.getElementById("dropdown-add");
        $('#search-add').attr('value',elem.selectedOptions[0].innerText);
        document.getElementById("search-add").value = elem.selectedOptions[0].innerText;

        
        $('#dropdown-add').hide();
    });



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
        var counter=0;
        var searchText = $(this).val().toLowerCase();
        $('#dropdown option').each(function () {
            var optionText = $(this).text().toLowerCase();
            if (optionText.indexOf(searchText) > -1) {
                $(this).show();
                counter++;
            } else {
                if(!$(this).is(":disabled"))$(this).hide();
            }
        });

        
        if(counter <= 1)counter = 2;
        if(counter > 10)counter = 10;
        $('#dropdown').attr('size', counter);
    });

    // Optional: Hide the dropdown when an option is clicked

    $('#dropdown').on('change', function () {
        elem = document.getElementById("dropdown");
        $('#search').attr('value',elem.selectedOptions[0].innerText);
        document.getElementById("search").value = elem.selectedOptions[0].innerText;
        $('#dropdown').hide();
    });
});